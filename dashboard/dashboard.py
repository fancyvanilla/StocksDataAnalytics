import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Supposons que vous avez déjà chargé vos données dans un DataFrame pandas appelé df
df = pd.read_csv('dashboard\\histo_cotation.csv')  # ou df = pd.read_csv(r'dashboard\histo_cotation.csv')

# Convertir les colonnes pertinentes en types de données numériques
columns_to_convert = ['QUANTITE_NEGOCIEE', 'CAPITAUX']  # Ajoutez d'autres colonnes si nécessaire
for column in columns_to_convert:
    df[column] = pd.to_numeric(df[column], errors='coerce')

columns_to_convert = ['NB_TRANSACTION']  # Ajoutez d'autres colonnes si nécessaire
for column in columns_to_convert:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# Calcul des KPIs
moyenne_valeur = df['QUANTITE_NEGOCIEE'].mean()
ecart_type_valeur = df['QUANTITE_NEGOCIEE'].std()
nb_transactions_total = df['NB_TRANSACTION'].sum()
capitaux_total = df['CAPITAUX'].sum()

# Initialisation de l'application Dash
app = dash.Dash(__name__)

# Mise en forme du layout du tableau de bord
app.layout = html.Div(children=[
    html.H1(children='Tableau de bord'),

    html.Div(children='''
        KPIs de l'entreprise:
    '''),

    html.Div(children=[
        html.Div(children=[
            html.H3('Moyenne de la valeur'),
            html.H4(f'{moyenne_valeur:.2f}')
        ], className='kpi'),

        html.Div(children=[
            html.H3("Écart-type de la valeur"),
            html.H4(f'{ecart_type_valeur:.2f}')
        ], className='kpi'),

        html.Div(children=[
            html.H3('Nombre total de transactions'),
            html.H4(f'{nb_transactions_total}')
        ], className='kpi'),

        html.Div(children=[
            html.H3('Total des capitaux'),
            html.H4(f'{capitaux_total}')
        ], className='kpi')
    ], className='kpi-container')
])

if __name__ == '__main__':
    app.run_server(debug=True)
