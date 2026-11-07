# Vorbereitung 14: ZIP-Prüfer + Sicherheitstests

**Nur Staging.** Keine Änderung an J.A.R.V.I.S., keine GitHub Actions auf `main`, keine Veröffentlichung.

`tools/inspect_release.py`: nur lesende Untersuchung vorhandener ZIPs; ungültige/Windows-gefährliche Dateipfade, doppelte Einträge, Symlinks, spezielle Dateien, ZIP-Bomben, CRC-Prüfung. Ergebnis enthält SHA-256, **keine** RSA-Signaturbestätigung.

`tests/test_inspect_release.py`: 10 Offline-Tests für den Prüfer. Im vollständigen Vorbereitungspaket 14: **33 lokale Tests bestanden**.

`JARVIS_CI_SICHERHEIT_VORBEREITUNG_14.zip` ist im Chat verfügbar (SHA-256: `33a9425925c8c7c4ff5439517419aee0aa4845082a77615e5b38e2ee5cef80f0`), mit zusätzlichem Quellen-Import, Kandidaten-Bau und GitHub-CI-Vorlagen. Kein echter v2.2.4-Gesamttest.

**Für später:** Code nur nach Prüfung in ein privates Source-Repo übertragen. Niemals einen unsignierten Kandidaten veröffentlichen oder mit diesem ZIP-Prüfer die RSA-Vertrauensprüfung ersetzen.