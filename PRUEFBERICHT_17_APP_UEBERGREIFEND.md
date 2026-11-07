# J.A.R.V.I.S. — übergreifende Fehlerkontrolle 17 (07.11.2026)

**Wichtig:** Geprüft wurden **lokal vorliegende ältere Jarvis-Quellpakete und vorbereitete, noch nicht installierte Erweiterungen**, nicht die aktuell auf dem Windows-Laptop installierte v2.2.4. Kein Laufzeittest auf dem Nutzer-PC; keine Veröffentlichung.

## Ergebnis reproduzierter Prüfungen
- Apps + Rechte (#16): `xvfb-run -a python -m unittest discover -s tests -p 'test_*.py' -q` → **83 bestanden**.
- Gmail-Papierkorb (#11): **12 bestanden**.
- CI-/ZIP-Sicherheit (#14): **33 bestanden**.
- Rekursive Quellcode-Inventur (#15): **12 bestanden**.
- **Insgesamt 140 lokale Tests bestanden**, mit Mocks und virtueller Linux-Tkinter-Anzeige, **nicht** mit echtem Discord/Spotify/Windows-Gmail-Konto.
- **47 Python-Dateien** aus den vier Modulverzeichnissen und zwei älteren ZIP-Quellcodepaketen per `ast.parse` geprüft → **0 Syntaxfehler**. Dies prüft weder Imports auf Windows noch Programmstart.
- In public GitHub Release zuletzt verifiziert: `v2.2.4`; das echte Update-ZIP konnte in dieser Umgebung nicht als lokal analysierbares Artefakt heruntergeladen werden.

## Bereits nachgewiesene Bugs, noch nicht behoben
1. Der Apps-Chat-Router erkennt `öffne Chrome` nicht als installiertes `Google Chrome` (fehlende Aliasauflösung).
2. Gültige Windows-App-Namen wie `C# Tools` oder `Python 3.13: Manuals` können die Apps-Freigabeoberfläche aufgrund zu strikter Namensvalidierung abbrechen.
3. Unbewilligter Chat-Befehl wirft `AccessDenied`; die spätere echte Jarvis-Chat-Integration muss diese Ausnahme abfangen und als freundliche Antwort ausgeben.

## Weitere konkret zu prüfende Risiken (kein Beweis eines laufenden Fehlers)
4. **Gmail-Schreib-OAuth-Schlüsselspeicher:** `gmail_trash._ring()` prüft, im Gegensatz zum Spotify-Modul, nicht den tatsächlich aktiven Windows-Keyring-Backend-Typ. Vor echter Gmail-Freigabe sicherstellen, dass Token niemals auf unverschlüsseltem Backend gespeichert werden.
5. **Release-Kompatibilität:** Ein vorliegendes älteres `updater.py` (v2.1.1) enthält feste Datei-Allowlists und verlangt `jarvis.py` in jedem Update. Neue Apps-, Musik- und Gmail-Moduldateien sind dort **nicht** enthalten. Prüfen, ob **v2.2.4** die erforderlichen signierten Modul-/Asset-Erweiterungen erlaubt; **nicht** zum Beheben die Signatur/Allowlist pauschal ausschalten.
6. **User-Freigaben und Identität:** Berechtigungen werden nach App-Namen gespeichert; vor produktiver Nutzung die Bindung an eine vertrauenswürdige Windows-App-ID/Verknüpfung prüfen. Sonst können gleichnamige Anwendungen/Verknüpfungen zur falschen App aufgelöst werden. Kein Beleg für eine aktuelle Ausnutzung.
7. **GUI-Hänger:** Spotify/Gmail-Netzwerkaufrufe müssen im integrierten Jarvis aus dem Tkinter-Hauptthread ausgelagert werden; sonst kann die Oberfläche bei langsamem Netzwerk einfrieren. Bestehende App-Router-Dokumentation weist darauf hin.
8. GitHub `updates/status.json` beschreibt weiterhin einen **nicht signierten v2.1.3-Plan**, während als öffentliches Release v2.2.4 vorliegt. Diese Datei darf **nicht** als produktiver Versions-/Signaturnachweis dienen.

**Priorität vor dem Produktiv-Release:** vorhandene drei Apps-Bugs reparieren, sichere Windows-Tokenablage prüfen, v2.2.4-Modul-/ZIP-Signaturintegration gegen echte aktuelle Quellen testen und erstmaliges E2E-Update auf dem Benutzer-Laptop durchführen. Keine voreilige Erfolgszusage.
