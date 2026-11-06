# J.A.R.V.I.S. Dateimanager Plus — Sammelfunktion 06

**Status:** Lokal als eigenständiger Einmal-Installer vorbereitet, 45 Tests bestanden; noch nicht auf dem Nutzer-Laptop installiert oder als signiertes GitHub-Release veröffentlicht.

- Dateianalyse: Größe, Typ, heuristische Wichtigkeit, begrenzte SHA-256-Duplikatsuche; nur lesend
- Bestehend: Dateien in frei gewählte Benutzerordner verschieben und in Windows-Papierkorb geben (nur nach Zustimmung)
- Neu: Ordner erstellen; Textdateien `.txt`, `.md`, `.log`, `.csv`, `.json` erstellen
- Neu: `.txt`/`.md`/`.log` in eine neue `.txt`/`.md` zusammenführen; CSV-Dateien nur bei identischen Kopfzeilen in neue CSV zusammenführen; Originale bleiben erhalten
- Schutz: Kein Überschreiben, System- und OneDrive-Ordner gesperrt, Installer legt Backup an und verweigert unbekannt veränderte Module
- Beschränkung: keine KI-Inhaltsklassifikation; PDF/DOCX-Zusammenführen noch nicht implementiert

Lokale Artefakte aus der Chat-Unterhaltung: `JARVIS_DATEIMANAGER_PLUS_EINMAL.pyw` (SHA-256 `966c8de436857dc46e5cd26b745f4f410be2fdc703bf8e219d35dc1c55ed04bb`) und `JARVIS_DATEIMANAGER_PLUS_SAMMELPAKET_06.zip` (SHA-256 `88fd20853755fc32147e1f04987fe3e2882174a33b239cbb2f4f9aba3f270b25`).

Vor einem gemeinsamen signierten Release ist Integration in den tatsächlichen Stand, Windows-Praxistest und lokal signierte Veröffentlichung nötig. Diese Notiz ist keine Installation.
