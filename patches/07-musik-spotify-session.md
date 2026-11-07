# Sammelfunktion 07 – Musikdesign + Spotify-Anmeldung

**Noch nicht installiert / veröffentlicht.** Bitte erst mit den anderen Erweiterungen gemeinsam signieren.

- Lokal vorbereitet: `JARVIS_MUSIK_SAMMELPAKET_SPOTIFY_LOGIN.zip`
- ZIP SHA-256: `c792dc042a84423684bbaf93ffd321cbc243ba18c713fc71838b293f2c828028`
- Bestehendes Musikdesign: sieben Kacheln, lokale PNG-Logos, Welle, Layout nach Referenzbild.
- Spotify-Kachel öffnet `https://open.spotify.com/` im **normalen Standardbrowser**, damit die Browser-Sitzung genutzt wird. Keine temporären Browserprofile, OAuth-Tokens oder Passwortspeicherung in Jarvis.
- Bei fehlgeschlagenem Browserstart erscheint eine verständliche Fehlermeldung.
- Spotify kann eine erneute Anmeldung verlangen; Anmeldung ist von Browser-Cookies abhängig, also keine Garantie auf ewiges Login.
- **11 GUI-/Funktionstests** auf lokalem Testsystem bestanden. Noch kein Test mit echtem Spotify-Konto.
- Für echte Kontosteuerung über Spotify Web API wäre später eine eigene OAuth-PKCE-Integration nötig. Diese ist bewusst nicht Teil dieses Pakets.
- Vor dem signierten Release die Musikseite in die aktuelle Jarvis-Version integrieren, neue Dateien in der Update-Freigabeliste prüfen und unter Windows starten.

Dieser Branch enthält ausschließlich den Hinweis; die ZIP-Datei wurde in der Chat-Unterhaltung erstellt, nicht als Release hochgeladen.
