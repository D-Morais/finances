from dash import html, dcc
import dash_bootstrap_components as dbc


# =========  Layout  =========== #
layout = dbc.Card([
    # ========= Seleção de Perfil ========= #
    html.H1("MyFinances", className="text-primary", style={"text-align": "center", "color": "blue", "margin-top": "10px"}),
    html.Hr(),
    dbc.CardImg(src="/assets/img_hom.png", alt="Avatar", className='perfil_avatar'),
    html.Hr(),
    dbc.FormFloating([
        dbc.Input(type="text", placeholder="Digite seu usuário", id="usuario"),
        dbc.Label("Usuário")
    ], style={"margin": "10px 20px"}),
    dbc.FormFloating([
        dbc.Input(type="password", placeholder="Digite sua senha", id="senha"),
        dbc.Label("Senha")
    ], style={"margin": "10px 20px"}),
    dbc.Row([
        dbc.Col([
            dbc.Button("Acessar", color="primary", id="acessar", style={"border-radius": "5px"})
        ], width=6),
        dbc.Col([
            dbc.Button("Novo Usuário", color="success", id="novo_usuario", style={"border-radius": "5px"})
        ], width=6)
    ], style={"margin-left": "20px", "margin-bottom": "10px"}),
], style={"width": "35%", "margin-left": "33%", "margin-top": "50px", "border-radius": "5px"})
