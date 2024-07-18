# auth.py
from dash import dcc
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from app import app

users = {"username": "password"}  # Define users and passwords (use a secure method in production)

def layout():
    return html.Div([
        dcc.Location(id='url_login', refresh=True),
        html.H2('Please log in to continue', id='h1'),
        dcc.Input(placeholder='Enter your username', type='text', id='uname-box'),
        dcc.Input(placeholder='Enter your password', type='password', id='pwd-box'),
        html.Button('Login', n_clicks=0, id='login-button'),
        html.Div(children='', id='output-state')
    ])

@app.callback(
    Output('url_login', 'pathname'),
    [Input('login-button', 'n_clicks')],
    [State('uname-box', 'value'), State('pwd-box', 'value')]
)
def success(n_clicks, input1, input2):
    if n_clicks > 0:
        if input1 in users and users[input1] == input2:
            return '/page1'
        else:
            return '/'

@app.callback(
    Output('output-state', 'children'),
    [Input('login-button', 'n_clicks')],
    [State('uname-box', 'value'), State('pwd-box', 'value')]
)
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        if input1 in users and users[input1] == input2:
            return ""
        else:
            return "Invalid username or password"
