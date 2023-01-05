import dash
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
from flask import send_from_directory

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import os
import flask
from random import randint
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
# from intro_tabs import consent, tutorial, form


server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=server,external_stylesheets=[dbc.themes.BOOTSTRAP,'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'])

# server = app.server

app.config.suppress_callback_exceptions = True

# app.layout = html.Div([
#     html.Div(id="lay",className="test"),
#     html.Div(id='page-content')

# ])


# @app.server.route('/static/<path:path>')
# def static_file(path):
#     static_folder = os.path.join(os.getcwd(), 'static')
#     return send_from_directory(static_folder, path)

# @app.callback(Output('page-content', 'children'),
#               [Input('lay', 'className')])
# def display_page(pathname):
#      if pathname == 'test':
#          return consent.layout
#      else:
#         return '404'

# if __name__ == '__main__':
#     app.run_server()