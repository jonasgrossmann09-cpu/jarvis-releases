# Letzter Codex-Auftrag: Danach J.A.R.V.I.S. über ChatGPT weiterentwickeln

**Status 07.11.2026:** Planung / Abnahmecheckliste, KEINE Änderungen an `main`, keine Version veröffentlicht. Dieses Dokument ist beim späteren „Kodex-Auftrag“ vorrangig zu verwenden. Funktionserweiterungen 01–12 nur als gesammelte Wünsche erhalten, aber NICHT als Blocker für die Infrastruktur behandeln.

## Verifizierter Ist-Stand (GitHub)
- Öffentliches Release-Repo `jonasgrossmann09-cpu/jarvis-releases`: `main` enthält `.github/`, `README.md`, `updates/`, aber **kein `src/`, `tests/` oder `tools/`**.
- `.github/workflows/jarvis-autorelease.yml` hängt an `release/request.json`, ruft fehlende Scripts `tools/check_windows.py` und `tools/build_release.py` auf, enthält einen `publish`-Job. **0 Workflow-Runs** auf GitHub bestätigt.
- Letztes öffentliches Release: **v2.2.4** mit `jarvis-2.2.4.zip`, `jarvis-update.json`.
- `jonasgrossmann09-cpu/jarvis-source` wurde in der angebundenen GitHub-Kontoansicht **nicht gefunden**; vorhandene Berechtigung dort nicht bestätigt.
- Chat-Vorbereitung `JARVIS_CHATGPT_OHNE_CODEX_EINRICHTUNG.zip` (vorhanden): sicherer initialer Quellcodeexport, Win-CI, unsignierter Kandidatenbauer. Das ist **nur Bootstrap**, keine Release-Pipeline. Der echte lokale Quellcode v2.2.4 befindet sich noch nicht in dieser GitHub-Verbindung.
- Vorhandener DPAPI-geschützter lokaler RSA-Signaturschlüssel **nicht auslesen, exportieren, ersetzen oder ChatGPT zusenden**.

## Einmaliger Codex-Auftrag: MUSS / in dieser Reihenfolge

### P0 Sicherung und Quellcode (Blocker)
1. Auf dem Windows-Laptop die **aktuelle funktionierende Installation** und alle persönlichen Daten **lokal vollständig sichern**; die Code-Dateien separat in einer überprüften Liste erfassen.
2. Mit vorhandenen lokalen Rechten das **private** Source-Repository `jarvis-source` erstellen. `gh`/GitHub login nur per offiziellem Browser/CLI-Login; niemals Zugangsdaten im Chat/Quellcode. `src/`, `tests/`, `tools/`, `docs/`, `pyproject.toml`/`requirements` und CI-Dateien anlegen. Keine `.env`, Secrets, DPAPI-Key, Gmail-/Spotify-Tokens, Logs, DBs, Modelle, Tagebuchdaten in Git.
3. Einen reproduzierbaren lokalen Start der **aktuellen** Jarvis-Version aus diesem Repository erreichen und sie mindestens einmal smoke-testen. Keine alten Beispielcode-Dateien über neuere echte App-Dateien legen.
4. GitHub-Anbindung für den **normalen ChatGPT-Chat** durch den Benutzer ausdrücklich für genau dieses private Repository freigeben. Spätestens hier zeigen, dass ChatGPT einen Änderungsvorschlag über den GitHub-Connector einreichen kann.

### P1 Tests / CI / Trennung von Secrets
5. PR-Tests unter `windows-latest` (Python-Syntax, Imports, Unit-Tests, Update-Sicherheit, Headless-/Smoke-Start auf Windows) **ohne Secrets und ohne Release-Schreibrechte**. Bei Fehler keine Merge-/Publish-Freigabe.
6. Nach menschlich bestätigtem Merge in den geschützten Hauptbranch gesonderten **Release-Job** erstellen. Änderungen am Build-/Signiercode dürfen nicht unbeobachtet an Secrets gelangen. Protection/Review für Release-Environment einsetzen. Kein `pull_request_target` mit untrusted Code.
7. Cross-Repo-Veröffentlichung **aus dem privaten Source-Repo** in das bestehende öffentliche `jarvis-releases` (GitHub App/eng begrenzter Fine-Grained Token, nur benötigte Repo-Rechte, nur Actions-Secret, NIE Client-Token).

### P2 Signaturen / Updater / Pilot-Release
8. Bestehendes tatsächliches Updateformat, Signatur-Payload, Public-Key-Anker, Manifest-/SHA-256-Prüfung und Pfad-/Allowlist-Regeln aus der aktuellen App analysieren. **Keine Kompatibilität erraten.**
9. Sichere Signierarchitektur einrichten: entweder streng isolierter Freigabe-/Signerprozess auf vertrauenswürdigem Windows-PC oder neuer CI-Signing-Key mit **über den bestehenden vertrauenswürdigen Schlüssel signiertem Übergangsupdate**; niemals die Signaturprüfung abschalten oder bisherige Schlüssel durch unsignierten Austausch ersetzen. Key für Cloud-CI nur in dafür geeigneter geschützter Secret-Umgebung, nicht in Logs/Repo.
10. Release nur bei allen Tests grün, freigegebenem Job und tatsächlich gültiger Signatur erzeugen; idempotent, kein Überschreiben bestehender Tags/Versionen. Korrektes öffentliches ZIP + Metadaten veröffentlichen.
11. Bestehenden Updater (nicht parallelen Neubau) so prüfen/ergänzen, dass er via öffentlicher HTTPS GitHub API findet, lädt, SHA/Signatur checkt, separat nach App-Ende installiert, persönliche Daten erhält, neu startet und im Fehlerfall vollständig rollbackt. Nicht ungefragt während aktiver Arbeit neu starten.

### P3 Ende-zu-Ende-Beweis (MUSS für „ohne Codex fertig“)
12. EINEN absichtlich winzigen ungefährlichen Testpatch **aus dem normalen ChatGPT-Chat** in `jarvis-source` einreichen.
13. Tests via GitHub Actions erfolgreich; Nutzer bestätigt PR/Merge und Freigabe; GitHub erstellt gültig **signiertes** Release im bestehenden öffentlichen Repository.
14. Lokaler Jarvis erkennt, validiert, installiert, startet und behält Settings/Daten. Teste außerdem manipuliertes ZIP, falsche Signatur, Downgrade, unterbrochene Installation/Rollback, doppelte Builds.
15. Kurze `DEVELOPMENT_WITH_CHATGPT.md`-Anleitung im **privaten** Repository: „Wie nehme ich künftige Änderungswünsche direkt im normalen ChatGPT-Chat vor?“ inklusive Repo-Adresse, Dateistruktur, PR/Review, Freigabe-Workflow, Troubleshooting, Kosten- und Secret-Hinweis.

## Fertigdefinition
Erst wenn 12–14 **nachweislich erfolgreich durchgelaufen** sind, ist das Ziel „keine Codex-Nutzung mehr für normale Jarvis-Änderungen und Releases“ erfüllt. Ohne aktives GitHub-Repo-Connector-Recht, private Quelle, passenden Signer und E2E-Test ist dies weiterhin nur **vorbereitet**, keine Garantie.

## Bewusst nachrangig
- Die 12 gesammelten J.A.R.V.I.S.-Funktionswünsche samt ZIPs und Designvorlagen im Chat bewahren; **erst über die fertige ChatGPT-/GitHub-Strecke** nachliefern.
- Wenn es risikolos passt, höchstens ein kleiner UI-Wunsch im Pilot-Release; Featureumfang niemals vor dem P0–P3-Infrastrukturziel priorisieren.
- Kein neues Release auf dem bisherigen `main` während der Infrastrukturvorbereitung ohne gesicherte Signier-/Rollbackfreigabe.
