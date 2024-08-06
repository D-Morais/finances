from dash.exceptions import PreventUpdate
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
from script_db import procura_usuario, adc_usuario

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
    html.Div(id="login-output", className="mt-2"),

    # Modal
    html.Div([
        html.Div([
            html.Span('x', id='close-modal', className='close', style={"margin-left": "5px"}),
            html.H2("Cadastrar usuário", className="text-primary", style={"text-align": "center", "color": "blue",
                                                                          "margin-top": "10px"}),
            html.Hr(),
            dbc.CardImg(src="/assets/img_hom.png", alt="Avatar", className='perfil_avatar'),
            html.Hr(),
            dbc.FormFloating([
                dbc.Input(type="text", placeholder="", id="reg_usuario", style={"border-radius": "5px"}),
                dbc.Label("Novo usuário")
            ], style={"margin": "10px 20px"}),
            dbc.FormFloating([
                dbc.Input(type="password", placeholder="", id="reg_senha", style={"border-radius": "5px"}),
                dbc.Label("Escolha sua senha")
            ], style={"margin": "10px 20px", "border-radius": "5px"}),
            dbc.Button("Adicionar", color="primary", id="adc_usuario",
                       style={"border-radius": "5px", "width": "30%", "display": "block", "margin": "0 auto"},
                       n_clicks=0),
            html.Div(id='reg-output-state')
        ], style={"width": "40%", "height": "90%", "margin-left": "30%", "margin-top": "30px", "border-radius": "5px",
                  "background-color": "#f1f1f1"}, className='modal-content')
    ], id='modal', className='modal')

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


# Callback para abertura do modal
@app.callback(
    Output('modal', 'style'),
    [Input('novo_usuario', 'n_clicks'), Input('close-modal', 'n_clicks')],
    [State('modal', 'style')]
)
def toggle_modal(reg_clicks, close_clicks, current_style):
    if reg_clicks or close_clicks:
        if current_style and current_style.get('display') == 'block':
            return {'display': 'none'}
        return {'display': 'block'}
    return {'display': 'none'}


# Callback para criação de novo usuário
@app.callback(
    Output('reg-output-state', 'children'),
    Input('adc_usuario', 'n_clicks'),
    [
        State('reg_usuario', 'value'),
        State('reg_senha', 'value')
    ],
)
def adc_novo_usuario(n_clicks, novo_usuario, nova_senha):
    if n_clicks:
        if novo_usuario and nova_senha:
            adc_usuario(novo_usuario, nova_senha)
            return dbc.Alert(f"Usuário adicionado com sucesso.", color="success", is_open=True, duration=2000)
        else:
            return dbc.Alert("Necessário preencher todos os campos.", color="warning", is_open=True, duration=2000)
