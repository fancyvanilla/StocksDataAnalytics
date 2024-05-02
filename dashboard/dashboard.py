import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Charger les données depuis un fichier CSV
df = pd.read_csv('dashboard\histo_cotation.csv')
# Convertir les colonnes pertinentes en types de données numériques
columns_to_convert = ['QUANTITE_NEGOCIEE', 'CAPITAUX', 'NB_TRANSACTION']  
for column in columns_to_convert:
    df[column] = pd.to_numeric(df[column], errors='coerce')
# Calcul des KPIs
total_transactions = df['NB_TRANSACTION'].sum()
total_capitaux = df['CAPITAUX'].sum()
nombre_entreprises = df['VALEUR'].nunique()

# Initialisation de l'application Dash
app = dash.Dash(__name__)

# Mise en forme du layout du tableau de bord
app.layout = html.Div(children=[
    html.H1(children='Tableau de bord'),

    html.Div(children='''
        Graphiques basés sur les données de l'entreprise :
    '''),

    # Graphique Pie basé sur les valeurs de la colonne 'VALEUR'
    dcc.Graph(
        id='graph-pie',
        figure={
            'data': [
                go.Pie(
                    labels=df['VALEUR'].value_counts().index.tolist(),
                    values=df['VALEUR'].value_counts().values.tolist()
                )
            ],
            'layout': {
                'title': 'Répartition des valeurs'
            }
        }
    ),

    # Graphique Bar basé sur les valeurs de la colonne 'SEANCE'
    dcc.Graph(
        id='graph-bar',
        figure={
            'data': [
                go.Bar(
                    x=df['SEANCE'],
                    y=df['QUANTITE_NEGOCIEE']
                )
            ],
            'layout': {
                'title': 'Quantité négociée par séance'
            }
        }
    ),

    # KPIs
    html.Div(children=[
        html.Div(children=[
            html.H3('Nombre total de transactions'),
            html.H4(total_transactions)
        ], className='kpi'),

        html.Div(children=[
            html.H3('Total des capitaux'),
            html.H4(f'${total_capitaux}')
        ], className='kpi'),

        html.Div(children=[
            html.H3('Nombre d\'entreprises'),
            html.H4(nombre_entreprises)
        ], className='kpi')
    ], className='kpi-container')
])

if __name__ == '__main__':
    app.run_server(debug=True)
