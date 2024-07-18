# pages/page1.py
import dash_bootstrap_components as dbc
from dash import html
from sidebar import sidebar

# Define o conteúdo principal
content = dbc.Col(
    [
        html.H1('Page 1'),
        html.A('Go to Page 2', href='/page2'),
        html.Br(),
        html.A('Logout', href='/'),
    ],
    style={"margin-left": "25%"}  # Adiciona margem para evitar sobreposição
)

# Define o layout
layout = dbc.Container(
    [
        dbc.Row(
            [
                sidebar,
                content
            ],
            style={"height": "100vh"}  # Altura total do viewport
        )
    ],
    fluid=True,
)
