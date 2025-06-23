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
    'Italy': 'lightblue',
    'South Korea': 'lightgreen',
    'United Arab Emirates': 'darkorange'
}

# Gruppenbildung (Ausgewählte Länder für Analyse)
g7 = ['United States', 'Germany', 'France', 'Canada', 'Japan', 'United Kingdom']
eu_core = ['Spain', 'Poland', 'Netherlands', 'Sweden', 'Italy']
extra_countries = ['China', 'India', 'Russia', 'Brazil', 'Vietnam', 'Malaysia', 'Singapore', 'United Arab Emirates', 'South Korea']

"""
Warum wird ein Land AUSGEWÄHLT:
✅ G7-Mitglied (immer dabei)
✅ EU-Kernland (immer dabei)
✅ Wichtiges Schwellenland (immer dabei)
✅ Top 10 GDP-Durchschnitt UND mindestens 5 Jahre Daten

Warum wird ein Land NICHT ausgewählt:
❌ Zu wenig Daten (< 5 Jahre GDP-Werte)
❌ Nur Nullwerte (sum_value = 0)
❌ Nicht in Top 10 GDP UND nicht in vordefinierter Liste
❌ Fehlende Farbe in country_colors (beim Plotten)
    """

# Alle wichtigen Länder kombiniert
all_selected_countries = sorted(set(g7 + eu_core + extra_countries))

# Verbesserte einheitliche Länderauswahl für alle Notebooks
def get_selected_countries(df, value_col='Total'):
"""
    Einheitliche Länderauswahl basierend auf Datenqualität und Abdeckung.
    Verwendet Durchschnittswerte statt Summen um Verzerrungen durch fehlende Jahre zu vermeiden.

    Diese Funktion wird in ALLEN Notebooks verwendet für konsistente Analysen.
    """
    try:
        if value_col not in df.columns:
            return all_selected_countries

        # Datenabdeckung pro Land analysieren
        country_stats = df.groupby('Country').agg({
            value_col: ['count', 'sum', lambda x: x.notna().sum(), 'mean']
        }).round(2)

        country_stats.columns = ['total_records', 'sum_value', 'valid_records', 'mean_value']

        # Länder mit ausreichender Datenabdeckung filtern
        min_records = 5  # Mindestens 5 Jahre Daten erforderlich
        quality_countries = country_stats[
            (country_stats['valid_records'] >= min_records) &
            (country_stats['sum_value'] > 0)
            ].index.tolist()

        # Top-Länder basierend auf Durchschnittswerten (weniger von fehlenden Jahren beeinflusst)
        top_by_mean = (country_stats[country_stats.index.isin(quality_countries)]
                       .nlargest(10, 'mean_value')
                       .index.tolist())

        # Kombination mit vordefinierten Ländergruppen
        final_selection = sorted(set(g7 + eu_core + extra_countries + top_by_mean))

        return final_selection

    except Exception as e:
        # Fallback zu statischer Liste
        return all_selected_countries