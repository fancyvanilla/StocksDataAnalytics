import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Charger les données depuis un fichier CSV
df = pd.read_csv('histo_cotisation.csv')

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
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
