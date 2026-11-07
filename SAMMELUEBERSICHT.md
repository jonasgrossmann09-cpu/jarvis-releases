# J.A.R.V.I.S. — Sammelpaket für späteren „Kodex-Auftrag“

**Status: ausschließlich gesammelt/vorbereitet. Nicht in der aktuellen App installiert und nicht als gemeinsames Release veröffentlicht.**

Aktuell bereits separat veröffentlicht: **2.2.4** (Musikmodul). Die Punkte unten dürfen nicht als bereits installierte Funktionen dargestellt werden. Zu jeder Position existiert eine Staging-Notiz; die ausführbaren ZIPs wurden in der Chat-Unterhaltung erstellt und sind **nicht** in GitHub hinterlegt.

| Nr. | Thema | Inhalt | Detail |
|---|---|---|---|
| 01 | Konfliktschutz | Ältere Installer dürfen neueren GitHub-Code oder Signaturschlüssel nicht überschreiben | [notiert](STAGING_NOTES.md) |
| 02 | Backups | Sicherungen vorsichtig bereinigen; mindestens fünf erhalten, nicht vor 60 Tagen | [notiert](STAGING_NOTES.md) |
| 03 | ZIP-Sicherheit | Pfadmanipulation, ZIP-Bomben, Symlinks, Spezialdateien und Dubletten abweisen | [Details](patches/03-zip-validation.md) |
| 04 | Gmail | Lesender Zugriff nach separater Google-OAuth-Freigabe, Einordnung von Nachrichten | [Details](patches/04-gmail-readonly.md) |
| 05 | Dateimanager | Dateien analysieren, Wichtigkeit heuristisch einschätzen, verschieben, Papierkorb nach Zustimmung | [Details](patches/05-dateimanager.md) |
| 06 | Dateimanager Plus | Ordner und Textdateien anlegen; Textdateien und passende CSVs zusammenführen | [Details](patches/06-dateimanager-plus.md) |
| 07 | Musikdesign und Login | Offline-Logos, optische Vorlage, Spotify und andere Dienste im Standardbrowser mit bestehender Browser-Anmeldung | [Details](patches/07-musik-spotify-session.md) |
| 08 | Entwicklerzentrale | Jarvis soll geprüfte Änderungspakete nach ausdrücklicher Freigabe testen, lokal signieren und selbst veröffentlichen | [Details](patches/08-entwicklerzentrale-release-manager.md) |
| 09 | Apps/Windows-Programme | Apps-Kachel öffnet Übersicht nach Referenz mit 24 Logos, Suche, Filtern, Programminfo, zuletzt geöffnet und Start normaler installierter Apps | [Details](patches/09-windows-programme.md) |
| 10 | Musikaktivität | Aktueller Windows-Medientitel; Spotify „läuft gerade“/„zuletzt gespielt“ nach eigener OAuth-Freigabe | [Details](patches/10-musikaktivitaet-spotify-windows.md) |

| 11 | Gmail-Papierkorb | Werbung/Social-Mails nur nach Einzel-Auswahl und Bestätigung in den Papierkorb verschieben; wichtige/markierte Nachrichten geschützt; separater OAuth-Zugriff | [Details](patches/11-gmail-papierkorb.md) |

| 12 | Dateisortierung per Gespräch | Jarvis fragt wie sortieren; thematisch zusammengehörige Dateien sammeln und nach Vorschau/Bestätigung als ZIP oder Ordner bündeln | [Details](patches/12-dialog-dateisortierung.md) |

| 16 | Apps-Zugriffsverwaltung | Pro App Schalter für chat-/sprachgesteuerten Start; Spotify aktuelle/letzte Titel mit OAuth, globaler Windows-Medienzugriff, Freigaben widerrufen; 83 Offline-Tests | [Details](patches/16-app-zugriffsverwaltung.md) |

## Grenzen und offene Punkte
- **Keine Installation oder gemeinsame Veröffentlichung bis zur ausdrücklichen Anweisung „Kodex-Auftrag“.**
- Die echten Windows-Integrations- und Gesamttests sind noch offen, auch wenn einzelne Modultests bereits bestanden.
- Spotify-Anmeldungen im Browser sind **nicht** gleichbedeutend mit API-Zugriff auf Hörverlauf. Dafür wird eine gesonderte Spotify-Freigabe benötigt.
- Gmail-Papierkorb ist **als isoliertes Modul programmiert und mit Mocks getestet**, aber noch nicht in J.A.R.V.I.S. installiert und nicht mit einem echten Gmail-Konto geprüft.
- Keine pauschalen „Zugriff auf alles“-Berechtigungen; zusätzliche Dienste nur mit tatsächlich vorhandenen Schnittstellen und klarer Nutzerfreigabe.
- Versionsbasis und Release-Stand beim späteren Auftrag neu prüfen; nicht blind 2.2.4 überschreiben oder Sicherheitslisten erweitern.

Bei „Kodex-Auftrag“: Alle Pakete und Wünsche 01–12 aus der Unterhaltung sammeln, mit der **aktuellen** installierten Version abgleichen, Backup erstellen, Konflikte klären, nur nötige Dateien ändern, alle Tests durchführen, signieren und **ein einziges** GitHub-Release veröffentlichen.
