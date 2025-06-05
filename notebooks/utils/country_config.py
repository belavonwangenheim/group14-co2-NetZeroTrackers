# notebooks/utils/country_config.py

# Farbzuweisungen für Länder
country_colors = {
    'China': 'red',
    'United States': 'blue',
    'India': 'orange',
    'Russia': 'green',
    'Japan': 'purple',
    'Germany': 'black',
    'Canada': 'brown',
    'United Kingdom': 'magenta',
    'France': 'cyan',
    'Brazil': 'teal',
    'Poland': 'olive',
    'Spain': 'darkblue',
    'Netherlands': 'gold',
    'Sweden': 'darkgreen',
    'Vietnam': 'darkred',
    'Malaysia': 'pink',
    'Singapore': 'grey',
    'United Arab Emirates': 'darkorange'
}

# Gruppenbildung (Ausgewählte Länder für Analyse)
g7 = ['United States', 'Germany', 'France', 'Canada', 'Italy', 'Japan', 'United Kingdom']
eu_core = ['Spain', 'Poland', 'Netherlands', 'Sweden']
extra_countries = ['Vietnam', 'Malaysia', 'Singapore', 'United Arab Emirates']

# Funktion für jedes Notebook, um die Top 10 globalen CO2-Emittenten dynamisch zu bestimmen
def get_selected_countries(df, value_col='Total'):
    top_emitters = df.groupby('Country')[value_col].sum().nlargest(10).index.tolist()
    return sorted(set(g7 + eu_core + top_emitters + extra_countries))