# Group14 – CO2 NetZero Trackers

This project analyzes global CO₂ emissions with the aim of evaluating progress toward net-zero targets by 2075. The analysis focuses on G7 countries, selected key EU member states, and other major contributors to global emissions. By examining historical trends, forecasting future developments, and identifying the most relevant sources of CO₂, the project aims to assess whether current trajectories align with international climate goals – and what actions may be necessary to close potential emission gaps.



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

### 💡 Note:
This project is tested with Python 3.10 and 3.11.


## 🔎 Datasets Used
**1. Global Fossil CO₂ Emissions by Country:**  
Annual CO₂ emissions by fuel type (coal, oil, gas, cement, etc.) since 1950.  
Source: https://www.kaggle.com/datasets/thedevastator/global-fossil-co2-emissions-by-country-2002-2022  
📁Raw file: `GCB2022v27_MtCO2_flat`  
📁Processed file: `co2_cleaned_total.csv`

**2. Energy Consumption and Generation:**  
Global energy consumption and production data by country and energy type (e.g. coal, oil, renewables) from 1965 to 2021.  
Source: https://www.kaggle.com/datasets/donjoeml/energy-consumption-and-generation-in-the-globe  
📁Raw file: `World Energy Consumption.csv`  
📁Processed `wec_cleaned.csv`  

**3. Our World in Data – CO₂ CSV:**  
Consolidated emissions dataset including population, energy use, and GDP metrics.  
Source: https://github.com/owid/co2-data  
📁Raw file:  
📁Processed file:  

**4. World Development Indicators:**  
World Bank data on GDP, population, and other economic indicators.  
Source: https://www.kaggle.com/datasets/theworldbank/world-development-indicators?resource=download
📁Raw file: `WDICountry.csv`  
📁Raw file: `WEDIData.csv`  
📁Raw file: `WDISeries.csv`  
📁Processed file: ``  

## 👥 Authors
Béla von Wangenheim  
Jana Tam Nhu Pham, 589159  
XXX  
XXX  