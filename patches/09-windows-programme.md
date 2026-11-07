# Sammelwunsch 09 – Windows-Programme / Apps-Modul

**Status: nur vorbereitet, NICHT installiert, NICHT als Release veröffentlicht.**

## Ziel
Beim Klick auf die Kachel **Apps** in J.A.R.V.I.S. öffnet sich innerhalb der bestehenden Oberfläche eine Windows-Programmübersicht möglichst genau nach dem vom Nutzer hochgeladenen Referenzbild.

## Vorbereiteter Inhalt (Chat-Paket)
- **ZIP:** `JARVIS_APPS_SAMMELPAKET_09.zip`
- **SHA-256:** `b065ecba93b20e798b2ef5ea5155d26f3a7cee7dcb30160045a87a35d39cc8ab`
- `jarvis_apps_page.py`: fertig vorbereitete Tkinter-Seite, Programmsuche, Filter, Sortierung, Info, zuletzt *über Jarvis* geöffnet, Schnellzugriff.
- `icons/`: **24 lokale PNG-Logos** aus dem vom Nutzer bereitgestellten Screenshot (auch offline sichtbar).
- `referenz.png`, `apps_ui_vorschau.png`, `INTEGRATION.md`, `integration_patch.py`, `tests/`, `CODEX_KURZAUFTRAG.txt`.
- Dynamische Erkennung echter Windows-Apps über Startmenü-`.lnk` und Microsofts `Get-StartApps`, statt fest 42 Installationen vorzutäuschen.
- App öffnen über vorhandene Windows-Verknüpfungen oder registrierte App-IDs ohne Shell-String-Ausführung.
- Programm-Verknüpfungen für fehlende Apps per ausdrücklich gewählter, geprüfter Startmenü-`.lnk` in `%LOCALAPPDATA%/JARVIS/apps_links.json` speichern.
- Zuletzt *durch Jarvis* gestartete App-Namen/Zeitstempel in lokaler `apps_recent.json` speichern, keine Accountdaten.
- Discord, Spotify, WhatsApp, Outlook etc. mit ihren normalen installierten Clients öffnen; die Client-/Browser-Sitzung verwaltet die jeweilige App. **Keine Garantie einer ewigen Anmeldung**, keine Jarvis-Passwort-, Cookie- oder Token-Speicherung.
- Optionale offizielle Weblinks nur nach separatem Benutzerklick.
- **24 Python-Tests + GUI-/Such-/Filtertests bestanden**. Einbindung in verfügbare ältere UI-Kopie getestet; **noch kein echter Windows-2.2.4-Test**.

## Vor dem späteren Release
Die aktuelle Jarvis-Installation **sichern**. UI-Adapter minimal in die tatsächliche Jarvis-Version integrieren; **keine alten UI-Dateien überschreiben**. Windows-Start der Apps, Navigation, Offline-Logos, bestehende Anmeldung, Updater-Allowlists für zusätzliche Python-/PNG-Dateien und Rollback testen.

**NICHT jetzt veröffentlichen.** Erst beim späteren Nutzerwort **„Kodex-Auftrag“** zusammen mit allen anderen gesammelten Wünschen integrieren und signiert veröffentlichen. Das ZIP liegt nur in der Chat-Unterhaltung, nicht in diesem GitHub-Branch.
