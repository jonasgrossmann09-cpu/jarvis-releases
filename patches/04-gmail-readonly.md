# J.A.R.V.I.S. – Gmail-Modul (Entwurf für Sammel-Update)

**Status:** Modul lokal entwickelt und mit Mock-Daten getestet; noch nicht in J.A.R.V.I.S. 2.1.2 integriert und nicht mit einem Gmail-Konto verbunden.

## Geplante Fähigkeiten
- E-Mails des heutigen Tages abrufen, bis zu 30 Nachrichten
- Nur Absender, Betreff, Empfangszeit und Gmail-Kategorien auswerten; keine Mailtexte oder Anhänge
- Wichtige Nachrichten und Werbung als **Vorschlag** einordnen
- Lokale Kurzzusammenfassung ohne Versand oder Löschung

## Absicherung
- Google OAuth Desktop-App, nur explizite Nutzerfreigabe
- Ausschließlich `gmail.readonly`, keine Schreibberechtigungen
- OAuth-Zugang nur im Windows-Anmeldetresor (`keyring`) speichern
- **Keine** Zugangsdaten, E-Mail-Inhalte oder Tokens in GitHub speichern
- Nur bei explizitem Button `Gmail verbinden` Autorisierung starten
- Nutzer muss für die Gmail API ein eigenes Google-Cloud-Projekt / OAuth-Client einrichten

**Lokale Tests:** 5 bestanden (mit simulierten Gmail API-Antworten; kein realer Konto-Zugriff).

**ZIP-Paket in Chat:** `JARVIS_GMAIL_SAMMELPAKET_04.zip`  
**SHA-256:** `d1a41b0f2929b54d78b2414b39e13d97e5b89abc2a4e02b5e416ef5c5e0cef0c`.

Vor einem signierten Release ist die Integration in den tatsächlich installierten J.A.R.V.I.S.-Code und ein lokaler, freiwilliger OAuth-Test erforderlich. Dieser Entwicklungszweig ist **keine** automatische Veröffentlichung.
