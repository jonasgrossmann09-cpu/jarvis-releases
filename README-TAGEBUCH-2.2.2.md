# J.A.R.V.I.S. 2.2.2 — Tagebuch-Kachel

**Nur vorbereitet, noch kein Release.** Der automatische Jarvis-Updater nimmt ausschließlich signierte Versionen an.

## Ziel
Beim Klick auf **Übersicht → Tagebuch** den lokalen Link `http://127.0.0.1:18767/` im Standardbrowser öffnen. Andere Funktionen unangetastet lassen.

## Integration für die vorhandene lokale Veröffentlichung
1. Den tatsächlich installierten v2.2.1-Quellcode sichern und zum Erstellen des Releases in eine **Kopie** überführen.
2. `python tools/patch_tagebuch.py "<Pfad-zum-JARVIS-Kopierordner>"` ausführen.
3. Falls der bestehende Aufruf anders aufgebaut ist, stoppt das Skript ohne Änderung. **Nicht** ganze ältere UI-Dateien über eine neuere Installation kopieren.
4. Test: `python -m unittest discover -s tests -p 'test_tagebuch.py'` (Entwicklungsdateien im gleichen Projekt bereitstellen), Start der Kopie und Klick auf Tagebuch; der Tagebuchserver muss lokal laufen.
5. Version auf 2.2.2 erhöhen, Releasepaket mit der **vorhandenen** lokalen Schlüsselsignatur erstellen, erlaubte Dateien und bestehendes Updateformat beibehalten, ZIP-Hash und Signatur prüfen.
6. Release `v2.2.2` mit `jarvis-2.2.2.zip` und `jarvis-update.json` über den vorhandenen GitHub-Veröffentlichungsprozess bereitstellen, dann per Jarvis-Autoupdater testen.
7. Kein privater Schlüssel in GitHub oder in ZIPs/Logs; Originalinstallation nicht vorzeitig verändern.

Die Funktion verwendet ausschließlich die Python-Standardbibliothek und benötigt keine neue Abhängigkeit.
