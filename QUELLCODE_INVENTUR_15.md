# Vorbereitung 15: J.A.R.V.I.S.-Quellcode vollständig inventarisieren

**Stand 7. November 2026. Nur Vorbereitung, nicht installiert, nichts veröffentlicht.**

## Warum
In der bisherigen Bootstrap-Vorlage `tools/source_preflight.py` werden Python-Dateien überwiegend nur auf oberster Ebene des Jarvis-Quellordners erfasst; zusätzliche `*.py`- und `*.pyw`-Module in Unterordnern können beim Import in `jarvis-source` übersehen werden. Dieser Befund ist wichtig, bevor GitHub aus einem womöglich unvollständigen Stand Updates produziert.

## Neues Paket
- In dieser Chat-Unterhaltung erstellt: `JARVIS_QUELLCODE_INVENTUR_15.zip`
- SHA-256: `4a0bf2fbe6fbf9559e076da1434671f4569d1223f4917282b2a4fe861aea8c18`.
- `INVENTUR_STARTEN.pyw`: Windows-Tkinter-Auswahl des installierten Jarvis-Ordners oder eines vorhandenen ZIPs; speichert auf Wunsch lokal einen JSON-Bericht.
- `tools/inventory_source.py`: rekursive, **nur lesende** Inventur, zeigt auch verschachtelte Python-Module; markiert Symlinks, Pfadangriffe, Case-Kollisionen, sensible Dateinamen und private/Dependency-Verzeichnisse; nimmt keine Kopie vor und lädt nichts hoch.
- `tests/test_inventory_source.py`: **12 Tests bestanden**, inklusive ZIP-Traversal, Symlinks, verschachtelte Python-Module, Windows-Gerätenamen und private Verzeichnisse.
- `beispiel_inventur_2.1.1.json`, `beispiel_inventur_althistorie.json`, `BEFUND.md`.

## Tatsächliche Tests
- Historisches, lokal vorhandenes Release `jarvis-2.1.1.zip`: **9 Python-Dateien** erkannt.
- Historisches `JARVIS_Quellcode_fuer_Codex.zip`: **9 Code-Dateien, 17 Bild-Assets, 3 andere Dateien** erkannt.
- **Aktuelles 2.2.4-ZIP nicht herunterladbar in dieser Umgebung**; es wurde nicht inventarisiert.
- Ergebnis **ist keine Freigabe zum Hochladen**, keine Inhalts-/Secret-Prüfung und erst recht keine Signaturprüfung.

## Nächster sinnvoller Schritt
Beim späteren Einrichten des privaten `jarvis-source`-Repositories zuerst diese Inventur **auf dem tatsächlichen installierten Jarvis-Ordner** ausführen; vollständige Code-/Abhängigkeitsliste und fehlende Unterordner prüfen. Geheimnisprüfung und ausdrückliche Bestätigung sind vor jedem Upload verpflichtend. Niemals den DPAPI-/RSA-Privatschlüssel oder persönliche Daten hochladen. Den bereits vorhandenen Updater nicht ersetzen.

Die Live-Version und öffentliche `main` bleiben durch diese Staging-Notiz unverändert.
