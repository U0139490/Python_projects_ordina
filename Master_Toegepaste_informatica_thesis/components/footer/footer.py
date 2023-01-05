import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from app import app

from dash.dependencies import Input, Output, State

button_lock = True  



navbar = dbc.Navbar(
    [

    dbc.Button("Finished",id="finishButton",  href='https://kuleuven.eu.qualtrics.com/jfe/form/SV_0IAgGaqr07NX4Ff', color="danger",disabled=True), 
    html.Div([dcc.Interval( 
            id='interval-component',
            interval=15000,  # in milliseconds
            max_intervals=1,
            n_intervals=0
            )]),
    ],
    color="#2A385B",
)
@app.callback([Output('finishButton', 'disabled'),
               Output('interval-component', 'interval')],
              [Input('interval-component', 'n_intervals'),])
def update_button(n):
    if(n==1):
        return [False,10000]


# @app.callback(Output('label1', 'children'),
#     [Input('interval-timer', 'n_intervals')])
# def update_interval(n):
#     return 'Time: ' + str(10-n) + ":00"



