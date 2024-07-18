import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dash_table
from dash import dcc
from dash import html
# from dash_bootstrap_templates import template_from_url, ThemeChangerAIO

from app import app


# =========  Layout  =========== #
layout = dbc.Col([

    # ========= Tabela de Receita ========= #
    dbc.Row([
        html.Legend("Tabela de receitas"),
        html.Div(id="tabela-receitas", className="dbc")
    ]),

    # ========= Seção de Receitas ========= #
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='graph-receitas', style={"margin-right": "20px"})
        ], width=9),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Receitas"),
                    html.Legend("R$ -", id="valor-receita-card", style={'font-size': '60px'}),
                    html.H6("Total de receitas")
                ], style={'text-align': 'center'})
            ], color="success")
        ], width=3, style={"margin-top": "70px"})
    ])
], style={"padding": "10px"})


# =========  Callbacks  =========== #