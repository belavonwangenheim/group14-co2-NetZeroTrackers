# Group14 – CO2 NetZero Trackers

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