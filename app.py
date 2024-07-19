from dash import Dash
import dash_bootstrap_components as dbc

estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
           "https://fonts.googleapis.com/icon?family=Material+Icons", dbc.themes.COSMO]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"


app = Dash(__name__, suppress_callback_exceptions=True, title="MyFinances", external_stylesheets=estilos + [dbc_css])
app.scripts.config.serve_locally = True
server = app.server
