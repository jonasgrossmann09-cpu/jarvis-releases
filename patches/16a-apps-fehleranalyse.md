# Apps-Modul 16: kurze tatsächliche Fehleranalyse (07.11.2026)

**Nur Analyse und vorgemerkte Korrekturen. Kein Release.** Geprüft wurde das **vorbereitete, nicht integrierte** Paket `JARVIS_APPS_ZUGRIFFE_SAMMELPAKET_16.zip` aus dem Chat, nicht die laufende Windows-App.

## Testbefund
- `xvfb-run -a python -m unittest discover -s tests -p 'test_*.py' -q`: **83/83 Tests bestanden** (nur Offline-/Mock-/virtuelle Display-Tests).
- Ohne virtuelle Anzeige scheitern **4 GUI-Tests** nur an fehlendem Display (`TclError: couldn't connect to display ':0'`); das ist ein Umgebungsproblem, kein nachgewiesener Windows-App-Fehler.

## Zwei reproduzierte Funktionsfehler
1. **Alias fehlt im Chat-Router**: Mit vorhandenem installierten `Google Chrome` und eingeschalteter `app.launch`-Freigabe funktioniert `Jarvis öffne Google Chrome`, aber `Jarvis öffne Chrome` meldet `Programm chrome wurde nicht gefunden`. Grund: `chat_access_router.handle_app_command` vergleicht ausschließlich `app.name`, obwohl `jarvis_apps_page.PROGRAMS` Startmenü-Aliasse besitzt. **Fix:** Whitelist-basierte kanonische Aliasauflösung vor Lookup; Konflikte eindeutig behandeln; nie rohe Nutzereingabe an Shell.
2. **Unerwartete gültige Appnamen lassen App-Zugriffsoberfläche abstürzen**: Ein installiertes Programm mit Namen `C# Tools` oder `Python 3.13: Manuals` wird von Windows-Entdeckung grundsätzlich erfasst, doch `app_access.normalize_app` wirft `ValueError`, da `APP_ID` Zeichen `#` und `:` ausschließt. `AppAccessWindow.render -> _build_app -> supported_capabilities` fängt dies nicht. Der Absturz wurde mit Tkinter unter Xvfb reproduziert. **Fix:** Persistente, eindeutige sichere App-ID (z.B. normalisierter Name mit erlaubtem erweiterten Namensbereich oder stabiler Hash aus vertrauenswürdiger Start-ID), UI nicht bei einem fehlerhaften Eintrag abbrechen; negative Tests ergänzen.

## Dritter Integrationsrisiko-Punkt
3. **Ungenehmigter Chatbefehl wirft `AccessDenied`**: `handle_app_command('Jarvis öffne Discord')` wirft bei fehlendem Schalter absichtlich eine Ausnahme statt einer freundlichen Chat-Antwort. Das muss die spätere echte Chat-/Sprach-Anbindung abfangen, sonst kann ein nicht abgefangener Handler eine UI-Aktion scheitern lassen. Die Integrationsstelle ist bisher nicht vorhanden/getestet. **Fix:** Definierter Fehlertext, niemals unbehandelte Ausnahme im UI-Eventloop.

**Weiter offen:** Realer Windows-Programmstart (Discord/Spotify usw.), dauerhafte Sitzungen, tatsächliche Jarvis-v2.2.4-Integration, Spotify-OAuth, vollständige Tests auf dem Nutzerlaptop. Keine Aussage, dass alle Apps bereits auf dem Nutzer-PC funktionieren.
