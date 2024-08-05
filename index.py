from dash import html, dcc
from dash.dependencies import Input, Output
from app import app
from pages import dashboard, despesas, receitas, sidebar, login

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard.layout
    elif pathname == '/despesas':
        return despesas.layout
    elif pathname == '/receitas':
        return receitas.layout
    else:
        return login.layout


if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
