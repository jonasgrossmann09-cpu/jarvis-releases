# J.A.R.V.I.S. – Sicherheitsarbeiten (noch kein Release)

**Status:** Sammlung für ein späteres signiertes Release. Nicht auf `main` mergen, bevor der Windows-Test und der Signatur-Test erfolgreich sind.

- Patch 01: Ein älterer Installer darf auf GitHub vorhandenen, abweichenden Sourcecode nicht überschreiben (12 lokale Tests bestanden).
- Patch 02: Backup-Bereinigung mit Vorschau, 60 Tagen Mindestaufbewahrung und mindestens fünf erhaltenen erfolgreichen Sicherungen. Kein Zugriff auf ausstehende, fehlgeschlagene oder zurückgerollte Updates (11 lokale Tests bestanden).

Lokales Paket: `JARVIS_SICHERHEIT_SAMMELPAKET_02.zip` aus dieser Unterhaltung, SHA-256 `a69ed327a665a9b8c00b6c332383629bb0e8f3762f8744273d71ba504c606d7b`.

Der aktuelle GitHub-Release-Kanal bleibt unverändert. Vor Integration muss die Sammlung mit der **tatsächlich installierten** J.A.R.V.I.S.-Version zusammengeführt und auf Windows getestet werden. Nicht eigenständig alte Sicherungen löschen.
