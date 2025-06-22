# Group14 – CO2 NetZero Trackers

Dieses Projekt entwickelt ein Machine Learning-Modell zur Vorhersage globaler CO₂-Emissionen und bewertet den Fortschritt in Richtung Net-Zero-Ziele bis 2075. Mit historischen Daten von 1960-2018 erstellen wir Prognosemodelle, um Emissionspfade zu projizieren und zu bewerten, ob aktuelle Trends mit internationalen Klimazielen übereinstimmen.  

Die Analyse kombiniert Wirtschaftsentwicklungsindikatoren mit Emissionsdaten, um robuste Prognosemodelle zu erstellen, die die komplexen Beziehungen zwischen BIP-Wachstum, Urbanisierung, Wirtschaftsstruktur und CO₂-Emissionen berücksichtigen.

## Projektziele

- **Emissionsprognosen**: Entwicklung von ML-Modellen zur Vorhersage von CO₂-Emissionen bis 2075
- **Net-Zero-Bewertung**: Bewertung der Wahrscheinlichkeit, Net-Zero-Ziele zu erreichen
- **Wirtschaftlich-Umwelt-Modellierung**: Integration von Wirtschaftsindikatoren als Prognose-Features
- **Szenario-Analyse**: Modellierung verschiedener Entwicklungs- und Politikszenarien
- **Datenbasierte Klimapolitik**: Quantitative Erkenntnisse für Klimaschutzplanung

## Machine Learning-Ansatz

## Trainingsstrategie
- **Trainingsperiode**: 1960 – 2010 (50 Jahre historischer Muster)
- **Validierungs-/Testperiode**: 2011 – 2018 (Modellvalidierung auf aktuellen Daten)
- **Prognosehorizont**: 2019 – 2075 (57-Jahres-Projektionszeitraum)

## Modellentwicklung

## Hauptmerkmale
- **Wirtschaftsindikatoren**: BIP, BIP pro Kopf, Wirtschaftsstruktur (Industrie/Dienstleistungen)
- **Energiequellen**: CO₂-Emissionen nach Brennstofftyp (Kohle, Öl, Gas, Zement, etc.)
- **Entwicklungsmetriken**: Bevölkerungswachstum, Handelsdaten
- **Ländercharakteristika**: Entwicklungsstadium, geografische Region


## Verwendete Datensätze

**1. Our World in Data - CO₂ und Energiedaten**  
Jährliche CO₂-Emissionen nach Land und Brennstofftyp von 1960-2018.  
📁 Rohdatei: `owid-co2-data.csv`  
📁 Verarbeitete Datei: `co2_energy_data.csv`  
*Quelle: https://github.com/owid/co2-data*

**2. World Development Indicators (WDI)**  
Relevante wirtschaftliche Entwicklungsindikatoren der Weltbank.  
Enthält BIP, Bevölkerung, Wirtschaftsstruktur (Industrie-/Dienstleistungsanteile) und Handelsdaten.  
📁 Rohdatei: `WDIData.csv`  
📁 Verarbeitete Datei: `economic_indicators.csv`  
*Quelle: https://www.kaggle.com/datasets/theworldbank/world-development-indicators*

## Authors
Béla von Wangenheim, 589289  
Jana Tam Nhu Pham, 589159  
XXX  
XXX  


## Anforderungen
- **Python 3.10 oder 3.11** (getestete Versionen)
- **Umgebung**: Jupyter Notebook

## 🔧 Setup

```bash
# clone the repository
git clone https://github.com/your-username/group14-co2-NetZeroTrackers.git
cd group14-co2-NetZeroTrackers
```
```bash
# Create and activate a virtual environment

# On Windows PowerShell
python -m venv venv
.\venv\Scripts\activate

# On macOS / Linux
python3 -m venv venv
source venv/bin/activate
```
```bash
# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```
```bash
# Start Jupyter Notebook
jupyter notebook
```