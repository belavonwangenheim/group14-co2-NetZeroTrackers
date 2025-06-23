# Projekt Pipeline - Detaillierte Beschreibungen

Dieses Projekt entwickelt ein Machine Learning-Modell zur Vorhersage globaler CO₂-Emissionen und bewertet den Fortschritt in Richtung Net-Zero-Ziele bis 2075. Mit historischen Daten von 1960-2018 erstellen wir Prognosemodelle, um Emissionspfade zu projizieren und zu bewerten, ob aktuelle Trends mit internationalen Klimazielen übereinstimmen.

Die Analyse kombiniert Wirtschaftsentwicklungsindikatoren mit Emissionsdaten, um robuste Prognosemodelle zu erstellen, die die komplexen Beziehungen zwischen BIP-Wachstum, Urbanisierung, Wirtschaftsstruktur und CO₂-Emissionen berücksichtigen.

## Projektziele

- **Emissionsprognosen**: Entwicklung von ML-Modellen zur Vorhersage von CO₂-Emissionen bis 2075
- **Net-Zero-Bewertung**: Bewertung der Wahrscheinlichkeit, Net-Zero-Ziele zu erreichen
- **Wirtschaftlich-Umwelt-Modellierung**: Integration von Wirtschaftsindikatoren als Prognose-Features
- **Szenario-Analyse**: Modellierung verschiedener Entwicklungs- und Politikszenarien
- **Datenbasierte Klimapolitik**: Quantitative Erkenntnisse für Klimaschutzplanung

## 01_data_exploration.ipynb
**Erste Datenanalyse und Qualitätsbewertung**

Führt eine umfassende explorative Datenanalyse (EDA) der CO2- und Wirtschaftsdatensätze durch:

- **OWID CO2-Daten verstehen**: Analysiert 12,862 Datenpunkte über 218 Länder (1960-2018)
- **Datenqualitätsprüfung**: Bewertet Vollständigkeit von CO2-Emissionen (95%), Energiedaten (67%) und GDP (72%)
- **Top-Emittenten identifizieren**: Ermittelt China, USA, Indien als Hauptakteure mit strategischer Länderauswahl
- **CO2-Quellen analysieren**: Aufschlüsselung nach Kohle (41.6%), Öl (31%), Gas (21.1%)
- **Zeitliche Trends bewerten**: Globales CO2-Wachstum von 9,149 Mt (1960) auf 35,475 Mt (2018)
- **Wirtschaftsindikatoren prüfen**: GDP-Verfügbarkeit und Strukturdaten für ML-Features

**Output**: Datenqualitätsbericht und strategische Länderauswahl für weitere Analyse.

---

## 02_data_preparation.ipynb
**Datenbereinigung und Feature Engineering für Machine Learning**

Bereitet Rohdaten systematisch für ML-Modelle vor:

### CO2 & Energie Daten (OWID):
- **Datenquelle**: Our World in Data CO2-Dataset direkt von GitHub
- **Zeitfilter**: Beschränkung auf 1960-2018 für ML-Training
- **Feature-Erstellung**: CO2 nach Quellen, Energieintensität, CO2-Intensität
- **Qualitätssicherung**: Nur Länder mit ISO-Codes, Entfernung von Aggregaten

### Wirtschaftsindikatoren (World Bank WDI):
- **Relevante Indikatoren**: GDP, Wirtschaftsstruktur (Industrie/Services), Handel
- **Datenstruktur**: Transformation von Wide- zu Long-Format für ML
- **Aggregate-Entfernung**: Bereinigung um regionale/institutionelle Gruppierungen
- **Konsistenz**: Einheitliche ISO3-Codes und Zeiträume

**Output**: Zwei saubere Datasets (`co2_energy_data.csv`, `economic_indicators.csv`) ready für ML-Pipeline.

---

## 03_data_visualization.ipynb
**Umfassende Visualisierung und historische Trendanalyse**

Erstellt professionelle Visualisierungen zur Mustererkennung und Trend-Analyse:

### CO2-Emissionen Analyse:
- **Zeitreihen-Plots**: Langfristige Emissionsentwicklung der strategischen Länder
- **Quellen-Breakdown**: Pie Chart und Stacked Area für Energieträger-Mix
- **Besondere Jahre**: Snapshots für 1989 (Mauerfall), 2008 (Finanzkrise), 2015 (Paris-Abkommen)

### Wirtschaftsentwicklung:
- **GDP-Entwicklung**: Zeitreihen der größten Volkswirtschaften (1960-2018)
- **Strukturwandel**: Evolution von Landwirtschaft → Industrie → Dienstleistungen
- **Historische Vergleiche**: BIP-Rankings in Krisenjahren

### Visualisierungs-Features:
- **Konsistente Farbkodierung**: Einheitliche Länderfarben über alle Plots
- **Robuste Datenprüfung**: Automatische Anpassung an verfügbare Jahre
- **Professionelle Formatierung**: Legenden, Grid, Tight Layout

**Output**: Vollständige visuelle Analyse der Daten als Basis für ML-Feature-Selection.

---

## utils/country_config.py
**Zentrale Konfiguration für strategische Länderauswahl**

Definiert einheitliche Standards für Länderauswahl und Visualisierung:

### Ländergruppen:
- **G7-Volkswirtschaften**: USA, Deutschland, Frankreich, Kanada, Japan, UK
- **EU-Kernländer**: Spanien, Polen, Niederlande, Schweden, Italien
- **Schwellenmärkte**: China, Indien, Russland, Brasilien
- **Asiatische Tiger**: Vietnam, Malaysia, Singapur, UAE, Südkorea

### Erweiterte Farbkonfiguration:
- **20 Länder** mit individuellen Farben für konsistente Visualisierung
- **Neue Ergänzungen**: Italien (lightblue), Südkorea (lightgreen)
- **Strategische Abdeckung**: Alle wichtigen Wirtschaftsregionen repräsentiert

### Intelligente Auswahlkriterien:
- **Datenqualität**: Mindestens 5 Jahre zuverlässiger Daten
- **Wirtschaftliche Relevanz**: Hohe GDP-Durchschnittswerte oder Wachstum
- **Klimarelevanz**: Bedeutende aktuelle oder zukünftige Emissionsbeiträge
- **Regionale Repräsentation**: Vielfältige geografische und Entwicklungsabdeckung

### Konfiguration:
- **Farbzuweisungen**: Konsistente Länderfarben für alle Visualisierungen
- **Auswahllogik**: Dynamische Kombination aus festen Gruppen und datenbasierten Top-Performern
- **Fallback-Mechanismen**: Robuste Behandlung fehlender Daten

**Output**: Einheitliche, wissenschaftlich fundierte Länderauswahl für das gesamte Projekt.

---

## Pipeline-Übersicht

```
Raw Data (OWID + World Bank)
         ↓
01_exploration → Daten verstehen, Qualität bewerten, Muster erkennen
         ↓
02_preparation → Bereinigen, Features erstellen, ML-ready machen
         ↓
03_visualization → Trends analysieren, Insights visualisieren
         ↓
Ready for ML Modeling (04_model_development.ipynb)
```

**Jeder Schritt baut systematisch auf dem vorherigen auf und bereitet optimal auf die ML-Modellierung vor.**

## 🤖 Nächste Phase: Machine Learning Pipeline

### 04_model_development.ipynb (geplant)
**Modell-Aufbau und Training für CO2-Prognosen bis 2075**

Die nächste Phase entwickelt ML-Modelle zur Vorhersage von CO2-Emissionen:

#### Daten-Zeitraum Strategie:
```
Trainingsdaten:    1960 – 2010  (50 Jahre historische Muster)
Validierung/Test:  2011 – 2018  (7 Jahre für Modell-Evaluation)
Prognose-Horizont: 2019 – 2075  (57 Jahre Zukunftsprognosen)
```

#### Trainingsansatz:
- **1960–2010 als Training**: Genug Daten um Muster, Trends und Saisonalitäten zu erkennen
- **2013–2018 als Test**: Simuliert den "echten" Use-Case - Vorhersagen für Jahre, die das Modell nie gesehen hat
- **Lücke 2011-2012**: Pufferzone zwischen Training und Test für robuste Evaluation

#### Geplante Modellierungsansätze:
- **Zeitreihen-Modelle**:  
- **Multivariate Regression**: Integration von Wirtschaftsindikatoren als Features
- **Ensemble-Methoden**: Kombination verschiedener Ansätze für robuste Prognosen
- **Feature Engineering**: CO2-Intensität, Energiemix, Wirtschaftsstruktur als Prädiktoren

#### Erwartete Deliverables:
- **Trainierte Modelle** für alle strategischen Länder
- **Validierungs-Metriken**  
- **CO2-Projektionen bis 2075** mit Konfidenzintervallen
- **Net-Zero Bewertung** - Wahrscheinlichkeit der Zielerreichung

**Ziel**: Quantitative Bewertung der Net-Zero-Machbarkeit bis 2075 basierend auf aktuellen Trends und Wirtschaftsindikatoren.