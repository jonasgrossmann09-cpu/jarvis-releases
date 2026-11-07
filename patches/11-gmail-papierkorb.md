# Sammelfunktion 11 — Gmail nach ausdrücklicher Bestätigung in Papierkorb verschieben

**Status:** Programmiert und lokal getestet. **NICHT** in J.A.R.V.I.S. installiert, kein Live-Gmail-Konto verbunden, **NICHT** veröffentlicht.

## Vorbereitetes Paket
- ZIP aus Chat: `JARVIS_GMAIL_PAPIERKORB_SAMMELPAKET_11.zip`
- SHA-256: `6bbb14b6e5ef13f89be59d03121bb0b0d664534ce6aac2508643c386def07e89`
- Python-Dateien: `gmail_trash.py`, `gmail_trash_ui.py`, `tests/test_gmail_trash.py`
- Enthält README, Minimal-Integration, requirements und Manifest mit Einzeldatei-Hashes.

## Verhalten
1. Vorhandenes Gmail-Lesemodul bleibt bestehen und wird nicht verändert.
2. Eigener Button für **Gmail-Papierkorb**. Neue, separate Google-OAuth-Freigabe mit `gmail.modify` erst nach ausdrücklichem Nutzerklick. Bestehendes `gmail.readonly`-Token wird nicht automatisch erweitert.
3. Nur Metadaten-Vorschau für höchstens 20 Werbe-/Social-E-Mails im Posteingang; wichtige, markierte, gesendete, Entwürfe und bereits gelöschte E-Mails ausgeschlossen.
4. Nutzer markiert jede zu verschiebende Mail selbst und bestätigt mit dem exakten Text **PAPIERKORB** im Dialog.
5. **Unmittelbar vor jeder Änderung** wird das richtige Google-Konto, Absender, Betreff, Empfangszeit und Gmail-Schutzlabels erneut verifiziert. Bei Abweichung: Überspringen.
6. NUR `users.messages.trash`, **kein** `delete`, `batchDelete`, `send` oder automatische Massenaktion. Bei API-Fehler werden Teilerfolge angezeigt, keine automatische Wiederholung.
7. OAuth-Token ausschließlich separat in Windows Credential Manager (`keyring`). Separates Trennen entfernt nur das Schreib-Token; bei Google kann Zugriff zusätzlich widerrufen werden.

**Grenze:** Googles erforderlicher `gmail.modify`-Scope ist technisch breiter als die hier eingebaute Papierkorb-Funktion (auch andere Gmail-Änderungen möglich). Ein spezieller Papierkorb-only-Scope existiert nicht; deshalb zusätzliche technische und UI-Sperren. Gmail API-Berechtigung und Testkonto erst später einrichten.

## Tests
- **12 Unit-Tests bestanden** (simulierte Google-Antworten: Vorschau/Schutz/Bestätigung/Kontowechsel/Teilfehler).
- **5 ältere Gmail-Readonly-Regressionstests bestanden**.
- **Tkinter-Oberflächentest bestanden**.
- **Offen:** echter Google-OAuth-Login, echte Gmail-Verschiebung, Windows-Integration.

**Für den späteren Gesamtauftrag:** ZIP aus dem Chat in eine gesicherte Kopie der aktuellen Jarvis-Installation integrieren, Freigabeliste für neue Python-Dateien anpassen, mit echtem Testkonto prüfen, dann gemeinsam mit anderen Sammelmodulen signiert veröffentlichen. Nicht jetzt mergen oder releasen.

Quellen:
- https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/trash
- https://developers.google.com/workspace/gmail/api/auth/scopes
