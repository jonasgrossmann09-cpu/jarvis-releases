# Sammelwunsch 08: J.A.R.V.I.S. Entwicklerzentrale / eigener Release-Manager

**Status:** Konkrete Spezifikation für das spätere Sammel-Update. Noch **nicht** in J.A.R.V.I.S. installiert und kein Release veröffentlicht.

## Ziel
Neue, **vorbereitete und vom Nutzer freigegebene** Code-Änderungen ohne Codex in der bestehenden Windows-Installation zu signierten GitHub-Releases machen. Danach übernimmt J.A.R.V.I.S. das bereits vorhandene automatische Update-System. Die KI entscheidet nie eigenmächtig, Code zu installieren oder zu veröffentlichen.

## Oberfläche (Einstellungen → Entwicklerzentrale)
- Schalter **Entwicklermodus** (standardmäßig aus).
- **Änderungspaket auswählen**: lokale Datei/ZIP oder geprüfter Arbeitsordner; nie blind Dateien aus dem Chat ausführen.
- **Änderungen prüfen**: Versionsnummer, Liste aller betroffenen Dateien, Dateiunterschiede, Größe, erlaubte Dateitypen, berechneter SHA-256.
- **Tests ausführen**: Syntax/Importe, bestehende Unit-Tests, Windows-Starttest aus einer isolierten Kopie, Sicherheitsprüfungen; Status und lesbare Fehlermeldungen anzeigen.
- **Release vorbereiten**: Sicherung, Paket erstellen, Manifest mit festem Repository-/Versions-Pfad und Datei-Hash, Signatur mit **bestehendem lokalem DPAPI-geschütztem privaten Schlüssel**. Signatur und Paket sofort mit dem gepinnten öffentlichen Schlüssel selbst prüfen.
- **Auf GitHub veröffentlichen**: Vorschau mit Tag, Versionsnummer, Dateiliste und Änderungsnotizen; separate ausdrückliche Bestätigung per Button **Jetzt veröffentlichen**. Ohne Bestätigung kein Upload, kein Tag, keine Änderung am laufenden Jarvis.
- **Status / Verlauf**: Link zum Release, Datum, Ergebnis, Fehler; Abbruch und erneutes Versuchen ohne doppeltes Release.
- Nach erfolgreich veröffentlichtem Release darf der bestehende Auto-Updater Version, Signatur und Hash wie bisher kontrollieren und sie beim Neustart installieren.

## Architektur
1. Vorhandene Skripte und den **bestehenden lokalen Veröffentlichungsvorgang** aus der tatsächlichen Windows-Installation wiederverwenden; minimaler GUI-Wrapper statt vollständiger Neuschreibung.
2. Herausgelöster Worker-Prozess für das Packen, Testen und Hochladen; Jarvis-Fenster bleibt ansprechbar.
3. GitHub-Anmeldung über offizielle `gh auth login` / vorhandene gh-Sitzung. Niemals GitHub-Zugangstokens, OAuth-Cookies oder Passwörter im Sourcecode, ZIP, öffentlichen Repo oder in Logs speichern. Bei abgelaufener Sitzung zur manuellen Anmeldung auffordern.
4. Release-Inhalt genau auf die aktuell installierte, gesicherte **Quellcode-Version** plus explizit ausgewählte Änderungen beschränken. Ausgehendes Paket nur aus erlaubten Python-Dateien, Ressourcen und genehmigten Abhängigkeiten. Keine persönlichen Dateien, `.env`, Tokens, Datenbanken, Gmail-/Spotify-Daten oder DPAPI-Schlüsselmaterial hochladen.
5. Versionsnummer auf Basis des aktuellen öffentlichen GitHub-Releases prüfen (Stand bei Erstellung der Spezifikation: v2.2.4). Keine Tags/Assets überschreiben. Bestehende Datei- und Modul-Allowlists unangetastet lassen; nötige Erweiterungen separat prüfen und genehmigen.
6. Vor dem Publizieren eine **Dry-Run**-Prüfung gegen Signatur, Datei-Hash, Manifest-/ZIP-Dateilisten, erlaubte Pfade, Pfad-Traversal, Symlinks und Signatur-Vertrauensanker. GitHub-Upload-Fehler eindeutig behandeln; bei unvollständigem Release nicht fälschlich Erfolg melden.
7. Falls eine KI Code erzeugt, ist dieser **unvertrauenswürdig** bis der Nutzer Änderungen und Testergebnis ausdrücklich freigibt. Keine automatische Shell-Ausführung allein aufgrund von Chat-Eingaben.
8. Relevante Backups erhalten und rollbackfähig bleiben. Nie die gerade laufende J.A.R.V.I.S.-Installation während der Veröffentlichung verändern.

## Minimale E2E-Tests
- Gültiges, zuvor akzeptiertes Update wird vollständig gepackt, signiert und hochgeladen; Jarvis erkennt es über den normalen Updatepfad.
- Kein Upload bei Testfehler, ungültigem Dateityp, fehlender Signatur, falschem Hash, unzulässigem Pfad, bereits existierender Versionsnummer oder fehlender Freigabe.
- Alte Quellcodeversion darf neuere Dateien nicht überschreiben.
- GitHub offline/abgemeldet → verständlicher Fehler, kein Erfolgsvortäuschen.
- Kein Lesen/Übertragen von privaten Schlüsseln oder persönlichen Daten; kein Upload ohne Nutzerklick.
- Windows-Starttest und anschließender Auto-Update-/Rollbacktest auf gesicherter Testkopie.

## Abgrenzung
- **Erstellen und Veröffentlichen vorbereiteter Änderungen**: Ziel dieser Funktion.
- **Jarvis programmiert eigenständig beliebige neue Funktionen**: separates, deutlich riskanteres Projekt, hier nicht enthalten.
- Keine Veröffentlichung, solange Tests/Signatur/Benutzerfreigabe nicht erfolgreich sind.

## Übergabe an späteren Codex-Gesamtauftrag
Diese Spezifikation zusammen mit den übrigen gesammelten Patches integrieren, mit dem tatsächlich installierten J.A.R.V.I.S.-Code abgleichen und erst dann als neues, signiertes Gesamtupdate veröffentlichen. Code- und Schlüsselbestand auf dem Laptop haben Vorrang vor Annahmen aus diesem Dokument.
