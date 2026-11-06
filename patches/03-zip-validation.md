# J.A.R.V.I.S. Sicherheitspatch 03: Update-ZIP-Prüfung

**Status:** Vorbereitet und lokal getestet; **nicht** in J.A.R.V.I.S. installiert oder als Release veröffentlicht.

Der aktuell vorliegende `updater.py` aus v2.1.1 hatte bereits eine Allowliste und Größenlimits. Dieser Zusatz schützt außerdem gegen:
- ZIP-Symlinks, Unix-Spezialdateien, doppelte Pfade und ungewöhnliche Kompressionsformate
- ZIP-Bomben anhand von Größen- und Kompressionsgrenzen
- Falsch deklarierte Dateigrößen und ungültigen Python-Code

**17 Sicherheits- und Regressionstests bestanden**, insgesamt mit Patch 01 und 02 **40 Tests**. Der Prüfer lässt `updater.py` unverändert, wenn der tatsächlich vorhandene Funktionscode nicht mit der getesteten Referenz übereinstimmt.

Paket aus dem Chat: `JARVIS_SICHERHEIT_SAMMELPAKET_03.zip`  
SHA-256: `df9e4811201bd318cb953607f50d6c6642a51e6b79b159420508e0c6747788dc`

**Vor dem Release erforderlich:** Mit dem tatsächlichen v2.1.2-Code zusammenführen, auf Windows testen, dann lokal signieren. Die Datei auf GitHub ist nur ein Entwicklungsprotokoll; kein Release-Asset und kein ausführbares Update.
