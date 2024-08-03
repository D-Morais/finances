from dash.exceptions import PreventUpdate
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from script_db import procura_usuario

# =========  Layout  =========== #
layout = dbc.Card([
    # ========= Seleção de Perfil ========= #
    html.H1("MyFinances", className="text-primary",
            style={"text-align": "center", "color": "blue", "margin-top": "10px"}),
    html.Hr(),
    dbc.CardImg(src="/assets/img_hom.png", alt="Avatar", className='perfil_avatar'),
    html.Hr(),
    dbc.FormFloating([
        dbc.Input(type="text", placeholder="Digite seu usuário", id="usuario", style={"border-radius": "5px"}),
        dbc.Label("Usuário")
    ], style={"margin": "10px 20px"}),
    dbc.FormFloating([
        dbc.Input(type="password", placeholder="Digite sua senha", id="senha", style={"border-radius": "5px"}),
        dbc.Label("Senha")
    ], style={"margin": "10px 20px", "border-radius": "5px"}),
    dbc.Row([
        dbc.Button("Acessar", color="primary", id="acessar", style={"border-radius": "5px", "width": "20%"},
                   n_clicks=0),
        dbc.Button("Novo Usuário", color="success", id="novo_usuario", style={"border-radius": "5px", "width": "30%"},
                   n_clicks=0)
    ], style={"margin": "10px 20px", "flex-direction": "row", "justify-content": "space-between"}),
    html.Div(id="login-output", className="mt-2")
], style={"width": "35%", "margin-left": "33%", "margin-top": "50px", "border-radius": "5px",
          "background-color": "#f1f1f1"})


def verifica_usuario(usuario, senha):
    dado_login = procura_usuario(usuario)
    if dado_login[0] == usuario and dado_login[1] == senha:
        return True
    else:
        return False


# ======== Calback =========
@app.callback(
    Output('login-output', 'children'),
    Input('acessar', 'n_clicks'),
    [
        State('usuario', 'value'),
        State('senha', 'value')
    ],
)
def logar(n_clicks, usuario, senha):
    if n_clicks:
        if not usuario:
            return dbc.Alert("Por favor, preencha o campo de usuário.", color="danger", is_open=True)
        if not senha:
            return dbc.Alert("Por favor, preencha o campo de senha.", color="danger", is_open=True)
        else:
            confirma_usuario = verifica_usuario(usuario, senha)
            if confirma_usuario:
                return dcc.Location(href='/dashboard', id='redirect')
            else:
                return dbc.Alert("Login falhou. Usuário ou senha incorretos.", color="danger", is_open=True)
    else:
        raise PreventUpdate
