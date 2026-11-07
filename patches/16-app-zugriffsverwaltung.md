# Sammelpaket 16 – Individuelle App-Zugriffe mit echten Freigabeprüfungen

**Status 07.11.2026: lokal programmiert und getestet, NICHT auf dem Nutzer-PC installiert oder als J.A.R.V.I.S.-Version veröffentlicht.**

## Artefakt
- Im Gespräch erstellte ZIP-Datei: `JARVIS_APPS_ZUGRIFFE_SAMMELPAKET_16.zip`
- SHA-256: `4d02a671aeb766a95c2fa23ca2b3be632ecff46dd82c6608e4482c4d76953f5f`
- 42 Dateien einschließlich der **24 Offline-App-Logos**, Programm-Übersicht, Zugriffsoberfläche, OAuth-Spotify-Leser, dokumentiertem Gatekeeper, Chatbefehl-Router, Tests.
- **83 lokale Unit-/GUI-/Regressionstests bestanden** (mit simuliertem Windows/Spotify; Tkinter mit virtueller Anzeige). **Keine** reale Spotify-Anmeldung, kein Live-Windows-Test, keine Integration in die tatsächlich installierte v2.2.4.

## Umsetzung
1. Im Apps-Modul erscheint **APP-ZUGRIFFE**, in jeder Programmdetailkarte **ZUGRIFF EINSTELLEN**.
2. Für die 24 Referenz-Apps und zusätzliche tatsächlich erkannte Programme ist `Jarvis darf diese App per Chat/Sprachbefehl starten` pro Programm schaltbar. **Default AUS**; nur gesicherte Windows-Startmethoden; manueller Nutzerklick auf „Öffnen“ ist davon unabhängig.
3. Für Spotify getrennte Leseberechtigungen **aktuell laufender Song** und **zuletzt gespielt**; weitere notwendige, ausdrückliche Spotify-**OAuth PKCE**-Freigabe über den offiziellen Browser; Token ausschließlich via Windows Credential Manager `keyring`.
4. Eigener globaler Schalter für aktuelle **Windows-Mediensitzung** (appübergreifend, kein historischer Verlauf).
5. Zentrale Klassen `PermissionStore` und `AccessGateway`: jede KI-/Chat-/Sprachaktion muss Berechtigung **direkt vor der Aktion** prüfen; ungültige/missing Datei bedeutet gesperrt; `Alle Zugriffe sperren` nach Rückfrage; Spotify-Konto zusätzlich trennbar.
6. Begrenzter `chat_access_router.py` für explizite Kommandos wie „Jarvis öffne Discord“; keine Shell-Interpretation oder beliebigen Befehle.
7. **Ehrliche Grenzen:** Andere Appkonten wie Discord, WhatsApp, Outlook, Browser etc. sind **nicht** pauschal auslesbar oder steuerbar. Jeweils echte offizielle APIs, separate OAuth-Berechtigungen und zusätzliche Adapter nötig. Discord-Self-Bots nicht unterstützen; keine privaten Discord-Nachrichten per heimlicher Userautomation. App-Start-Berechtigung ist nicht Datenzugriff.
8. Nur lokale Booleans, **keine** Passwörter, Cookies, Tokens, privaten Daten oder Verlaufssammlung im Berechtigungsspeicher.

## Wichtige spätere Integration
- Auf **aktuellem** Jarvis-Code mit Backup und Tests basieren; Paket #16 ersetzt/ergänzt Sammlungen **#09 Apps** und **#10 Spotify-Musikaktivität**, nicht blind alte Dateien überschreiben.
- Bestehende Chat-, Sprach- und Musikpfade müssen tatsächlich an `AccessGateway` angeschlossen werden. Altes `ActivityPage` darf nicht eigenständig die neuen Permission-Prüfungen umgehen.
- Neue Dateien/PNG in den **signierten** Update-Allowlist aufnehmen, Windows-Start/OAuth/Abmelden/Allow/Deny/Updater-Rollback real testen.
- **Erst nach** der erfolgreichen ChatGPT→GitHub→signierter Jarvis-Selbstupdate-Infrastruktur ausliefern, so wie der Nutzer es priorisiert hat.
- Diese Notiz auf GitHub enthält **nicht** den ausführbaren Inhalt der ZIP; dieser liegt als Anhang der Unterhaltung vor.

Offizielle Hinweise:
- https://developer.spotify.com/documentation/web-api/reference/get-the-users-currently-playing-track
- https://developer.spotify.com/documentation/web-api/reference/get-recently-played
- https://support.discord.com/hc/de/articles/115002192352-Automatisierte-Benutzeraccounts-Self-Bots
