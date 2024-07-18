# sidebar.py
import dash_bootstrap_components as dbc
from dash import html

sidebar = dbc.Col(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P("A simple sidebar layout", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page1", active="exact"),
                dbc.NavLink("Page 2", href="/page2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    width=3,  # Aproximadamente 1/4 da página
    style={"position": "fixed", "height": "100%", "padding": "20px", "background-color": "#f8f9fa"},
)
