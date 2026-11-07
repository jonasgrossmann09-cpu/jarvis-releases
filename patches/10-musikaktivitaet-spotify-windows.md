# Sammelfunktion 10 – Musikaktivität / zuletzt gespielter Titel

**Status:** Eigenständige lokale Implementierung vorbereitet, nicht integriert, nicht mit Konto verbunden, nicht signiert oder veröffentlicht.

## Nutzerziel
Jarvis soll bei Wunsch sehen können, welcher Song gerade auf dem Laptop läuft und welche Titel zuletzt auf Spotify gespielt wurden. Künftig weitere Apps nur mit einzelnen, ausdrücklich freigegebenen offiziellen Schnittstellen integrieren, **keine pauschalen Zugriffsrechte**.

## Vorbereitetes ZIP-Paket
- `JARVIS_MUSIK_AKTIVITAET_SAMMELPAKET_10.zip` (in dieser Chat-Unterhaltung)
- SHA-256: `bbbaa8d2ce1ca1c51c359d743daab1dd635e3fe6f7ad40d83114241cf4983713`
- `spotify_readonly.py`: OAuth2-PKCE mit lokalem Callback, Spotify `/me/player/currently-playing` und `/me/player/recently-played` (nur zwei Leserechte); sicheres Tokenlager im Windows-Anmeldespeicher via `keyring`, automatisches Refresh, Fehlerbehandlung, kein Logging sensibler OAuth-Daten.
- `music_settings.py`: speichert nur die öffentliche Spotify-Client-ID im lokalen Jarvis-AppData-Ordner (keine Zugangsdaten).
- `windows_media.py`: aktueller Windows-Medientitel über optionale WinRT-`winsdk`-Schnittstelle, sofern vom jeweiligen Programm unterstützt.
- `activity_page.py`: Tkinter-Seite mit `Spotify verbinden`, `Trennen`, `Was läuft gerade?`, `Zuletzt gehört` und `Windows-Medien`.
- `tests/`: **16 lokale Tests einschließlich Tkinter-Oberflächentest bestanden** (simulierte API-Antworten und Mock-Anmeldespeicher). Reale Spotify- und Windows-Wiedergabe noch nicht auf dem Benutzer-Laptop getestet.

## Zugriff und Grenzen
- Spotify-Web-Login im Standardbrowser und eigene OAuth2-PKCE-Freigabe; nur `user-read-currently-playing` und `user-read-recently-played`. Der Browser-Login allein genügt nicht, um die API verwenden zu dürfen.
- Für ein neues Spotify-Developer-Projekt im Entwicklungsmodus kann ein **Premium-Abo des App-Besitzers** erforderlich sein; API-Verfügbarkeit nicht garantieren.
- Andere Dienste (Discord, YouTube Music, Apple Music, Spotify-fremde Appkonten) liefern keine vollständigen Aktivitäten ohne eigene Autorisierung und vorhandene offizielle APIs. Windows-Mediensitzungen zeigen nur den aktuellen Status unterstützter Apps, **keinen vollständigen historischen Verlauf**.
- Keine automatische Hintergrundüberwachung oder Archivierung; nur Abfragen bei Nutzeraktion. Account-Daten, Tokens und private Schlüssel niemals im GitHub-Repo speichern.

## Für den späteren „Kodex-Auftrag“
1. Paket aus dieser Unterhaltung zusammen mit Sammlungen #07 Musikdesign und #09 Apps in eine **gesicherte Kopie** der aktuell installierten Version integrieren.
2. In bestehender Musikseite nur einen Button für `ActivityPage` hinzufügen, andere Logos, Funktionen und Sitzungen behalten.
3. Optionale vertrauenswürdige Abhängigkeiten `keyring` und `winsdk` kontrolliert installieren und Update-Allowlist für neue Python-Dateien erweitern.
4. Spotify Developer Client-ID und OAuth-Redirect `http://127.0.0.1:8765/callback` erst nach freiwilliger Einrichtung; niemals Zugangsdaten anfordern.
5. Windows-Start, Consent/Trennen, echte Spotify-API, Betrieb ohne Internet, Fehlermeldungen und Rollback testen, dann mit den restlichen Sammeländerungen als ein signiertes Release veröffentlichen.

**Nicht jetzt veröffentlichen.** GitHub enthält hier nur diese Arbeitsnotiz, nicht den ausführbaren Quellcode.
