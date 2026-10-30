"""
Pipeline de analisis: orquesta persistencia de sesiones,
entrenamiento/recarga del detector, scoring y generacion de alertas.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, List, Tuple

from analytics.anomaly_detector import (
    AnomalyDetector, MODEL_VERSION,
    severity_from_score, reason_from_components,
)
from store.database import insert_session, get_trusted_serials
from store.anomaly_store import (
    get_config, insert_alert, get_all_sessions, get_alerted_session_ids,
    save_model_state, load_latest_model_state,
)

logger = logging.getLogger(__name__)

# Antiguedad maxima (horas) de una sesion para que pueda generar alerta. Las
# sesiones reconstruidas del historial forense (de hace dias) sirven para el
# analisis retrospectivo, pero no deben generar alertas "en vivo" de
# dispositivos que ya no estan conectados.
_ALERT_MAX_AGE_H = 24


def persist_sessions(
    sessions: List[Dict[str, Any]],
    serial_to_id: Dict[str, int],
) -> List[Tuple[int, Dict[str, Any]]]:
    """Inserta sesiones en BD; devuelve lista (session_id, session)."""
    saved: List[Tuple[int, Dict[str, Any]]] = []
    for s in sessions:
        serial = s.get("_serial", "")
        device_id = serial_to_id.get(serial)
        if not device_id:
            continue
        record = {
            "device_id":    device_id,
            "connected":    s.get("connected"),
            "disconnected": s.get("disconnected"),
            "drive_letter": s.get("drive_letter"),
        }
        sid = insert_session(record)
        record["serial"] = serial
        saved.append((sid, record))
    return saved


# Si llegan al menos estas sesiones nuevas desde el ultimo entreno, se
# reentrena el modelo aunque exista uno persistido valido.
_RETRAIN_SESSION_DELTA = 10


def _train_new() -> AnomalyDetector:
    """Entrena un modelo desde las sesiones de BD y lo persiste."""
    detector = AnomalyDetector()
    train_days = int(get_config("anomaly.train_days", "7") or "7")
    detector.train(get_all_sessions(), train_days=train_days)
    save_model_state(MODEL_VERSION, detector.to_payload())
    return detector


def load_or_train_detector(force_retrain: bool = False) -> AnomalyDetector:
    """
    Devuelve un detector reutilizando el modelo persistido cuando es posible.
    Reentrena (y persiste) solo si:
      - se fuerza,
      - no hay modelo guardado o esta corrupto,
      - la version del modelo es antigua,
      - han aparecido bastantes sesiones nuevas desde el ultimo entreno.
    """
    if force_retrain:
        logger.info("Reentreno forzado del modelo.")
        return _train_new()

    state = load_latest_model_state()
    if not state or not state.get("payload"):
        logger.info("Sin modelo persistido: entrenando uno nuevo.")
        return _train_new()
    if int(state.get("version") or 0) != MODEL_VERSION:
        logger.info("Version de modelo distinta: reentrenando.")
        return _train_new()

    try:
        detector = AnomalyDetector.from_payload(state["payload"])
    except (json.JSONDecodeError, KeyError, ValueError) as exc:
        logger.warning("Estado de modelo corrupto: %s. Reentrenando.", exc)
        return _train_new()

    current = len(get_all_sessions())
    if current - detector.n_sessions() >= _RETRAIN_SESSION_DELTA:
        logger.info("%d sesiones nuevas desde el ultimo entreno: reentrenando.",
                    current - detector.n_sessions())
        return _train_new()

    logger.info("Modelo reutilizado (v%s, %d sesiones).",
                state.get("version"), detector.n_sessions())
    return detector


def _is_recent(connected: Any, cutoff: datetime) -> bool:
    """True si la sesion comenzo despues de 'cutoff'. Sin fecha valida -> False."""
    if not connected:
        return False
    try:
        return datetime.strptime(str(connected), "%Y-%m-%d %H:%M:%S") >= cutoff
    except (ValueError, TypeError):
        return False


def score_and_alert(
    detector: AnomalyDetector,
    saved_sessions: List[Tuple[int, Dict[str, Any]]],
    serial_to_id: Dict[str, int],
) -> List[Dict[str, Any]]:
    """
    Aplica el detector a cada sesion nueva y genera alertas.
    Respeta el modo:
    - aprendizaje: no genera alertas
    - monitorizacion / estricto: inserta alertas que superen el umbral
    """
    mode = (get_config("anomaly.mode", "aprendizaje") or "aprendizaje").lower()
    if mode == "aprendizaje":
        logger.info("Modo aprendizaje: no se generan alertas.")
        return []

    threshold = float(get_config("anomaly.threshold", "0.6") or "0.6")
    trusted = get_trusted_serials()
    ya_alertadas = get_alerted_session_ids()
    cutoff = datetime.now() - timedelta(hours=_ALERT_MAX_AGE_H)
    alerts_created: List[Dict[str, Any]] = []

    for session_id, session in saved_sessions:
        # No re-alertar una sesion ya procesada en analisis anteriores
        if session_id in ya_alertadas:
            continue
        # Solo sesiones recientes: las historicas no generan alertas "en vivo"
        if not _is_recent(session.get("connected"), cutoff):
            continue
        # Los dispositivos de confianza (allowlist) no generan alertas
        if session.get("serial") in trusted:
            continue
        result = detector.score(session)
        score = result["score"]
        severity = severity_from_score(score, threshold)
        if not severity:
            continue
        components = result["components"]
        reason = reason_from_components(components)
        device_id = serial_to_id.get(session.get("serial", ""))
        alert = {
            "device_id":  device_id,
            "session_id": session_id,
            "severity":   severity,
            "score":      score,
            "reason":     reason,
            "components": json.dumps(components),
        }
        insert_alert(alert)
        alerts_created.append({**alert, "components_dict": components})

    logger.info("Alertas generadas: %d (modo=%s, umbral=%.2f).",
                len(alerts_created), mode, threshold)
    return alerts_created
