# Sammelwunsch 12 – Intelligente Dateisortierung im Dialog

**Wunsch vorgemerkt, noch nicht programmiert / installiert.** Diese Funktion erst **nach** der erfolgreich getesteten ChatGPT-ohne-Codex-Infrastruktur entwickeln.

## Ziel / Dialog
- Nutzer: „Jarvis, sortier meine Dateien.“
- Jarvis: „Wie möchtest du sie sortiert haben?“
- Nutzer: „Alles, was mit Jarvis zu tun hat, in einen Ordner oder in eine ZIP.“
- Jarvis durchsucht **nur vom Nutzer freigegebene Ordner**, schlägt anhand von Namen, Pfaden und Inhaltsindizien passende Dateien vor und zeigt eine übersichtliche Liste einschließlich Größe und Zielpfad.
- Jarvis fragt nach Ordner **oder** ZIP sowie dem Zielordner. Bei Unklarheit Rückfrage statt eigener Entscheidung.
- Erst nach **expliziter Bestätigung** das Paket erstellen bzw. Dateien verschieben. Standard: **ZIP nur als Kopie, Originale bleiben erhalten**; Verschieben nur nach gesonderter Bestätigung.
- Dateikonflikte und gleichnamige Dateien sicher behandeln; vollständiges Protokoll, Abbrechen und Rückgängig-Funktion bei Verschiebungen.

## Sicherheitsgrenzen
- Nicht ganz C:\, Windows-Systemordner oder geschützte Anwendungsdaten automatisch verschieben.
- Nicht auf Grundlage eines Stichworts beliebige aktive Jarvis-Programmdateien, Registry- oder laufende Konfigurationsdateien ändern.
- ZIP auf sichere Dateipfade prüfen; keine Symlink-Folgen, keine ZIP-Bomben, keine stillschweigende Löschung.
- Dateisammlung kann persönliche oder geheime Daten enthalten: Vorschau und Freigabe vor jeder Veröffentlichung/Weitergabe. Keine Datei automatisch nach GitHub hochladen.
- Vor jeder tatsächlichen Aktion die Pfade und Berechtigungen erneut validieren.

Diese Funktion erweitert später den bereits geplanten Dateimanager, statt einen parallelen unkontrollierten Dateizugriff zu schaffen.
