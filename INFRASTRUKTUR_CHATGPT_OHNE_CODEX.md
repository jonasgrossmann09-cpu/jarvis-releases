# J.A.R.V.I.S. – Entwicklung vollständig über ChatGPT (Infrastrukturauftrag)

Stand: 07.11.2026. **Keine Änderung an ausgelieferter App oder dem Release-Kanal.**

## Bereits lokal vorbereitet
- `JARVIS_CHATGPT_OHNE_CODEX_EINRICHTUNG.zip` (in der Chat-Unterhaltung)
- SHA-256: `5c099d29435e99e4d43f5947c74973a42548d6c16c2057d4c9028379e048ef87`
- Enthalten: `START_HIER.pyw` für sichere Quellcodekopie und explizit bestätigten **privaten** GitHub-Import; Windows-CI mit Quellcode-/Syntaxprüfungen; geprüfter **unsignierter** Kandidatenbauer; Tests, Dokumentation und Sicherheitsplan.
- **11 lokale Tests erfolgreich.** Das Beispielrelease v2.1.1 wurde beim Importfilter erkannt. Echte Version 2.2.4 muss auf dem Benutzer-PC exportiert werden; weder installiert noch auf GitHub übertragen.
- Der Setup-Import darf nur Code und bekannte Bildressourcen kopieren, keine JSON-Konfiguration, Zugangsdaten, privaten Schlüssel, Musik-/Tagebuchdateien oder Nutzerdaten. Es fordert vor jedem Netzwerk-Upload eine eigene Bestätigung.

## Noch nicht erledigt
1. Benutzer muss einmalig das echte, aktuell installierte JARVIS in ein neues privates `jonasgrossmann09-cpu/jarvis-source` übertragen; diese Chat-Sitzung kann keine privaten lokalen Laptopdateien lesen und besitzt keinen GitHub-Repo-Erstellen-Befehl. Das Setup versucht die Repo-Erstellung über lokal angemeldete `gh`-CLI.
2. Zugriff der ChatGPT-GitHub-Anbindung auf das neue Repository ausdrücklich genehmigen.
3. CI auf GitHub wirklich ausführen und mit echter Windows-Installation testen.
4. Den vorhandenen DPAPI-geschützten RSA-Schlüssel **nicht** veröffentlichen oder blind ersetzen. Für automatische GitHub-Signaturen ist ein sorgfältig signierter Vertrauensanker-Übergang zu einem separaten, nur per geschützter CI-Umgebung nutzbaren Schlüssel erforderlich. Der bisherige lokale Updater muss den neuen Schlüssel vorab signiert akzeptieren.
5. Eine sichere, zweckgebundene GitHub-App / Fine-Grained-Token mit Freigabe **nur** für `jarvis-releases` als Secret hinterlegen. Geheimnisse nicht in Client oder Source.
6. Nach bestätigtem Merge automatischen Paketbau, volle Testinstallation/Anti-Rollback und Veröffentlichung ergänzen; bis dahin kein signiertes Release.
7. GitHub Actions für private Repos hat Kontingent und eventuell Kosten; vor Aktivierung prüfen.

## Sicherheitsprinzipien
- PR-Checks laufen **ohne** GitHub-Releases-Zugang und ohne Signaturgeheimnisse.
- Veröffentlichen nur nach erfolgreichem Merge und geschützt freigegebenem Job.
- Signatur-, Hash- und Pfadprüfungen bleiben aktiv; kein unsigniertes Release.
- Keine Datenlöschung, nur Testinstallation aus einer gesicherten Kopie.
- Automatische Updates auf dem PC weiter über bestehenden Updater, keine zweite parallele Update-Lösung.
