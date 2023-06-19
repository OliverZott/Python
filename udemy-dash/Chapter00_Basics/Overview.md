# Tools overview

## Matplotlib

- **Urvater** aller Python-Visualisierungsbibliotheken
- Nach Vorbild von **Matlab - Plotfunktionen**
- Erzeugt **statische Visualisierungen**
- Fast alle **Diagrammtypen** sind möglich

## Seaborn

- verwendet **Matplotlib** im Backend
- **Schönere** Diagramme aber auch statisch

## Pandas

- Hauptzwecke: Datenanalyse und -manipulation
- Verwendet **Matplotlib** im Backend durch einfache `.plot()` -Funktionen
- Begrenzter Umfang der Diagrammtypen / und nur statuische Visualisierungen
- "Adhoc-Analysen"

## Plotly

- Firma und OpenSource Bibliothek
- Bibliothekt für JS, React, R und Python
- Interactive Plots als HTML files (**kein dynamisches einlesen** von Dateien)

## Dash

- Interagieren mit Diagrammen
- Anstatt einfacher HTML wird eine **Dashboard-Webanwendung** mit lokaler URL generiert
- Im Hintergrund läuft ein **Flask-Server**
- Dashboard kann deployed on online bereitgestellt werden
