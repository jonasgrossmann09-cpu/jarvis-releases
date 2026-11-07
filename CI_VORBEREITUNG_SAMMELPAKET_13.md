# J.A.R.V.I.S. – CI-Vorbereitung 13, vor letztem Codex-Auftrag

**Stand 07.11.2026.** Dieses Dokument liegt nur im Staging-Branch. **Kein Release und keine Änderung an der laufenden Anwendung.**

## Offline fertig und verifiziert
- Vorhandenes Bootstrap-Paket erweitert: **JARVIS_CI_VORBEREITET_OHNE_CODEX_13.zip**, SHA-256: `fc62683cc91973ce94abb91cd541cc77035b57ecdd1b249be8ad810849c793ca`. Download liegt als Datei in dieser Chat-Unterhaltung. Es ersetzt die vorherige Bootstrap-Vorlage, nicht die installierte App.
- `tools/source_preflight.py`: Quellcode-, Importumfang- und Geheimnisvorprüfung, keine Vollständigkeitsgarantie.
- `.github/workflows/ci.yml`: PR-/Main-Windows-CI ohne Signatur-/GitHub-Schreibrechte. **Noch nicht auf GitHub ausgeführt**.
- `tools/build_candidate.py`: reproduzierbares **UNSIGNIERTES** ZIP mit Datei-Hashes, niemals direkt als Jarvis-Update ausliefern.
- **NEU** `tools/verify_candidate.py`: ZIP-/Report-/Quellhash-Konsistenz; verwirft Zip-Slip, Backslash-/absolute Pfade, doppelte/unbekannte Einträge, verdächtige Kompression, Symlinks und Spezialdateien.
- **NEU** `tests/test_verify_candidate.py`: 12 zusätzliche Sicherheitstests, insgesamt **23 lokale Unit-Tests erfolgreich**.
- **NEU** `.github/workflows/candidate-dry-run.yml`: manuell startbarer Windows-Dry-Run für Build + Validierung ohne Signing-Secrets oder Veröffentlichung.
- **NEU** `docs/CODEX_NUR_NOCH_REST.md`: kurz gehaltener priorisierter Restauftrag.
- Der komplette Beispielablauf `build_candidate → verify_candidate` wurde lokal an einer künstlichen Zweidateien-Demo erfolgreich getestet. **Nicht** mit der echten Jarvis-Installation.

## Letzter Codex-Einsatz – exakt was noch offen ist
1. Vollständige aktuelle Jarvis-Installation auf dem PC inventarisieren, sicher lokal sichern, **alle** Source-Module übernehmen und in ein **privates** `jarvis-source`-GitHub-Repository übertragen. Die Bootstrap-Exportfunktion kopiert nur bestimmte Hauptmodule/Assets; auf zusätzliche Unterordner prüfen. OAuth, Tagebuch, persönliche Daten, DPAPI-Schlüssel etc. keinesfalls exportieren.
2. GitHub-Connector für den normalen ChatGPT-Chat auf das private Repository freigeben und Mini-PR **über ChatGPT selbst** nachweisen.
3. Bestehendes Update-/RSA-Format aus dem tatsächlichen installierten Code analysieren und **ohne Signatur-Abschaltung** eine sichere CI-Signierung mit überprüftem Vertrauensanker, geschütztem Approval-Environment und Repo-beschränktem Token zum öffentlichen Release-Repo einrichten.
4. Echte Windows-PR-CI und reales signiertes GitHub-Release erstellen, Updater lädt und installiert es nach Validierung. Anti-Rollback, negative Signatur-/ZIP-Tests und Recovery einschließlich persönlicher Daten nachweisen.
5. Nur wenn der komplette **ChatGPT → GitHub PR → CI → signierter Release → realer Jarvis-Selbstupdate**-Pfad funktioniert, ist das Ziel erreicht, Codex nicht mehr zu benötigen.

**Die 12 gesammelten Produkt-Funktionen erst danach schrittweise hinzufügen.** Nicht versuchen, sie vor dem Infrastruktur-Test in ein letztes überfrachtetes Release zu packen.

## Ehrlicher Status
23 Tests sind **offline** und nur am Bootstrap-Code. Weder GitHub Actions noch die laufende Jarvis-App wurden dadurch getestet. Kein signiertes Produktiv-Release erstellt, kein echter Signaturschlüssel verwendet.
