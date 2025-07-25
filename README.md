# Group14 – CO2 NetZero Trackers

### Projektbeschreibung

Dieses Projekt zielt darauf ab, den langfristigen Verlauf von CO₂-Emissionen führender Länder zu analysieren und zu prognostizieren – mit dem Ziel, die Erreichbarkeit von Netto-Null-Emissionen bis 2050 zu bewerten. Auf Basis historischer CO₂-Daten (Our World in Data) und ökonomischer Indikatoren (World Bank WDI) werden datengetriebene Modelle entwickelt, um Emissionspfade unter verschiedenen Zukunftsszenarien zu simulieren. Neben klassischen Machine Learning-Verfahren (Random Forest) kommen auch sequenzielle Deep Learning-Ansätze (LSTM) zum Einsatz. Das Projekt orientiert sich am CRISP-DM-Prozess und umfasst die vollständige Pipeline von Datenaufbereitung bis zur szenariobasierten Modellbewertung.

Der Fokus liegt auf ausgewählten Ländern (z.B. China, Deutschland, USA, Indien etc.), für die jeweils historische Emissionen analysiert und zukünftige Entwicklungen simuliert werden. Die Resultate liefern quantitative Einschätzungen zur Realisierbarkeit internationaler Klimaziele.

### Modellierungsansätze

Zur Umsetzung wurden zwei verschiedene Modellarchitekturen eingesetzt:

- **Random Forest (Multi-Output):**  
  Ein robustes Ensemble-Verfahren, das die vier Hauptquellen von CO₂ separat prognostiziert (`CO2_coal`, `CO2_oil`, `CO2_gas`, `CO2_cement`). Die aggregierte CO₂-Gesamtemission (`CO2_total`) wurde anschließend aus diesen Komponenten berechnet. Random Forest erlaubt interpretierbare Modellierung ohne starke Annahmen über Zeitstruktur.

- **LSTM (Long Short-Term Memory):**  
  Ein rekurrentes neuronales Netz, das speziell auf die Analyse zeitlicher Abhängigkeiten ausgelegt ist. Auch hier wurden die vier Emissionskomponenten separat vorhergesagt, `CO2_total` wurde nachträglich berechnet. LSTM ist besonders geeignet, um über längere Zeiträume komplexe Verläufe zu modellieren.

**Hinweis:** In beiden Modellansätzen wurde `CO2_total` **nicht direkt vorhergesagt**, sondern stets **aus den separat prognostizierten Komponenten berechnet**, um gezielte Eingriffe auf Ebene einzelner Emissionsquellen zu ermöglichen.

### Trainingsstrategie & Modellierung

- **Random Forest:**  
  Trainiert auf Daten bis 2010, evaluiert von 2011–2017. Die Inputfeatures umfassen wirtschaftliche Indikatoren sowie gezielt erstellte Lag-Features (z.B. `GDP_lag1`, `Energy_intensity_lag1`). Optional wurde ein Rolling Average mit Fenstergröße 3 zur Glättung verwendet. Bewertet mit RMSE, MAE und R².

- **LSTM:**  
  Trainiert mit sequenziellen Eingabefenstern (10 Jahre) auf skalierten Daten. Verwendet wurden Basis-Features und doppelte Lags (z.B. `GDP_lag1`, `GDP_lag2`). Das Netzwerk bestand aus zwei LSTM-Schichten (64 + 32 Units) mit Dropout. Zeitlich sauberer Split: Training bis 2005, Test bis 2017, mit EarlyStopping.

Beide Modelle wurden **pro Land separat** trainiert und getestet.

### Szenarien: Business-as-Usual (BAU) vs. Emissionsreduktion durch Maßnahmen

Um die Auswirkungen politischer und wirtschaftlicher Interventionen auf den Emissionsverlauf abzuschätzen, werden zwei Szenarien gegenübergestellt:

- **Szenario A – Business-as-Usual (BAU):**  
  Dieses Szenario projiziert die zukünftigen Emissionen auf Basis der durchschnittlichen jährlichen Wachstumsraten von 2013–2017. Es spiegelt einen Fortlauf der aktuellen Trends ohne zusätzliche klimapolitische Maßnahmen wider.

- **Szenario B – Mit Maßnahmen:**  
  In diesem Szenario werden gezielte Emissionsreduktionen angenommen, die ab definierten Zeitpunkten (z.B. 2018, 2025, 2030) einsetzen. Die jährlichen CO₂-Wachstumsraten werden hierbei angepasst, um ambitionierte Klimaziele wie das Pariser Abkommen zu modellieren.

Der Vergleich dieser beiden Szenarien ermöglicht eine datenbasierte Einschätzung, ob bestehende Trends ausreichen, um Net-Zero-Ziele zu erreichen – oder ob strukturelle Eingriffe notwendig sind.

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

## Projektstruktur und Dateibeschreibungen

| Datei | Beschreibung                                                                                                   |
|-------|----------------------------------------------------------------------------------------------------------------|
| `01_data_preparation.ipynb` | Bereinigung und Kombination der Rohdaten für die ML-Nutzung.                                                   |
| `02_data_understanding.ipynb` | Explorative Datenanalyse und Prüfung der Datenqualität.                                                        |
| `03_data_visualization.ipynb` | Visualisierung historischer Emissionstrends und wirtschaftlicher Indikatoren.                                  |
| `04_prognose_China-rf.ipynb` | Random-Forest-Prognose für China (mehrkomponentig mit Szenarien).                                              |
| `04_prognose_China-lsmt.ipynb` | LSTM-Modell für China mit Szenarienvergleich.                                                                  |
| `05_prognose_Germany-lsmt.ipynb` | LSTM-Modell für Deutschland mit Szenarienvergleich.                                                            |
| `06_prognose_usa-lsmt.ipynb` | LSTM-Modell für United States mit Szenarienvergleich.                                                          |
| `00_merge_lsmt_results.ipynb` | Zusammenführung der LSTM-Ergebnisse mehrerer Länder. Ergebniss in (final_result_bau und final_result_measures) |
| `data/processed/` | Bereinigte Datenquellen (`co2_energy_data.csv`, `economic_indicators.csv` etc.)                                |
| `data/results/` | Prognose-Ergebnisse aus den Modellen (BAU & Maßnahmen) als CSV.                                                |

## Authors
Béla von Wangenheim, 589289  
Jana Tam Nhu Pham, 589159  
Elisa Khoury, 589942

## Anforderungen
- **Python 3.10 oder 3.11** (getestete Versionen)
- **Umgebung**: Jupyter Notebook oder `.py`-Skripte
- **Entwickelt mit**: IntelliJ IDEA (Python Plugin)
- **Hinweis für VS Code**:  
  Bei Ausführung in **Visual Studio Code** kann es notwendig sein, **Pfadangaben wie**
  ```python
  df = pd.read_csv('../data/processed/germany_model_dataset.csv')
    ```
  zu ändern in z.B.:
  ```python
    df = pd.read_csv('data/processed/germany_model_dataset.csv')
    ```

## 🔧 Setup

```bash
# clone the repository
git clone https://github.com/your-username/group14-co2-NetZeroTrackers.git
cd group14-co2-NetZeroTrackers
```
```bash
# Create and activate a virtual environment

# On Windows PowerShell
py -3.11 -m venv venv
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