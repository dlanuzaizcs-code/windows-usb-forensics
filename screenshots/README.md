# Reviewed visuals (selected subset)

Only 3 review-selected images from the supplied screenshots are included in this staging package:

- `architecture-six-layers.png`: conceptual architecture diagram.
- `experiment-1-threshold-metrics.png`: results of the separated-class synthetic experiment.
- `experiment-2-roc.png`: ROC curve from the overlapping-class synthetic experiment.

PNG files were re-encoded without original metadata. These images contain no visible device identifiers or TOTP QR codes in the reviewed previews. **A manual final review is still required** before public release.

## Originals deliberately omitted

- `10.x_TOTP.png`: contains a TOTP enrollment QR and provisioning URI; **must never be published**. Rotate the TOTP secret if it is still in use.
- Other application screenshots show potentially identifying USB serial numbers, device identifiers, usernames or timestamps. Their publication requires redaction and separate review.
- No raw Windows artifact files, database records, audit logs or generated HTML/JSON reports are included.

The included charts are reported historical thesis results using **synthetic datasets**; they are not current production performance measurements.
