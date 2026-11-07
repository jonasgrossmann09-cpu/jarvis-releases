# Apps-Modul: 3 bestätigte Fehler in Sammelpaket 16B behoben

**Status 07.11.2026:** Quellcode in einem **neuen ZIP** korrigiert, lokal getestet. **Noch nicht in der installierten J.A.R.V.I.S.-Version integriert, nicht auf GitHub als Update veröffentlicht.** Diese Notiz ersetzt den Fehlerstatus aus `16a-apps-fehleranalyse.md`, **nicht** die tatsächliche Windows-End-to-End-Abnahme.

## Korrigiertes, vollständiges Paket
- **`JARVIS_APPS_ZUGRIFFE_FEHLERFREI_16B.zip`** – liegt als Download in der Chat-Unterhaltung, enthält Programmübersicht, 24 Offline-Logos, Berechtigungsoberfläche, Spotify-Freigaben, geänderte Tests und Manifest.
- SHA-256 des ZIPs: `d5c966fefa18f9a49e5af4f347cd0a85a690ca6931f614a9c923c023ff1eebcc`
- **43 Dateien inklusive `MANIFEST.json`**, alle Einzelhashes geprüft. Paket enthält die vollständige ältere vorbereitete Version #16 **mit** den 3 Korrekturen; beim späteren Import nicht 16 und 16B gleichzeitig mischen.

## Die drei Fixes
1. **App-Aliasse:** `chat_access_router.py` löst `Jarvis öffne Chrome` über die vordefinierte Liste in `jarvis_apps_page.PROGRAMS` sicher in `Google Chrome` auf. Explizite Programmnamen gehen vor; mehrdeutige Treffer werden abgewiesen. Nur tatsächlich bekannte, lokal registrierte App-Records können gestartet werden. Ohne Schalter weiterhin verboten.
2. **Gültige Programmnamen:** `app_access.py` erlaubt Windows-Namen wie `C# Tools`, `Python 3.13: Manuals`, `R&D @ Home` und Kommas. Pfadseparatoren, Kontroll-/Formatzeichen und überlange IDs bleiben gesperrt. `app_access_ui.py` zeigt auch problematische Einträge an, ohne beim Rendern abzustürzen; ungültige Freigaben bleiben gesperrt.
3. **Freundliche Fehlermeldungen:** `chat_access_router.py` fängt `AccessDenied` für Startbefehle, Spotify-Song- und Verlaufskommandos ab; Chat/Sprachoberfläche erhält eine verständliche Antwort, kein unbehandelter UI-Fehler. Fehlender Programmstart erzeugt ebenfalls eine Antwort. Ausgeschaltete Rechte führen weiterhin zu **keiner Aktion**.

## Tests und Grenzen
- Basis vorher: **83 Tests**.
- Neu: **11 Regressionstests**, insgesamt **94/94 lokale Tests** erfolgreich, inklusive GUI mit virtueller Tkinter-Anzeige, Alias-Mehrdeutigkeit, ungültigen Namen, Berechtigungspflicht und Verweigerung.
- 15 Python-Dateien ohne Syntaxfehler.
- Noch keine reale Windows-App-Installation getestet und **keine** Integration in die tatsächlich installierte J.A.R.V.I.S. v2.2.4. Der vollständige Sicherheitstest der Releases und OAuth-Provider bleibt ausstehend.
- Berechtigungen nach App-Anzeigenamen sind nur eine **Jarvis-App-Ebene** und keine Windows-/OAuth-Vollzugriffsbefugnis. Später überprüfte stabile App-IDs für doppelte/gleichnamige Programme vor produktiver Nutzung erwägen.

**Für den späteren Infrastruktur-/Gesamtauftrag:** Paket #16B statt #16 als aktuelle vorbereitete Apps-Version verwenden, die drei korrigierten Module mit aktuellem Quellcode abgleichen, alle 94 Tests erneut unter Windows durchführen, die Chat- und Sprachintegrationsstellen anbinden sowie die signierte Updater-Allowlist geprüft erweitern. Keinesfalls Signaturprüfung abschalten.
