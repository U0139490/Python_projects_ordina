import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from app import app

from dash.dependencies import Input, Output, State

button_lock = True  

search_bar = dbc.Row(
    [   
        dbc.Col(
        html.H3(id='label1', children='',style={"color":"white"}),
        width="auto"),
        
        html.Div([dcc.Interval( 
        id='interval-timer',
        interval=1000,  # in milliseconds
        max_intervals=10,
        n_intervals=0
        )]),

        dbc.Col(
        dbc.Button("Finished",id="finishButton",  href='https://kuleuven.eu.qualtrics.com/jfe/form/SV_0IAgGaqr07NX4Ff', color="danger", className="ml-2",disabled=True), 
        width="auto"),

        html.Div([dcc.Interval( 
        id='interval-component',
        interval=10000,  # in milliseconds
        max_intervals=1,
        n_intervals=0
        )]),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            # dbc.Row(
            #     [
            #         dbc.Col(html.Img(src='assets/wineLogo3.png', height="60px")),
            #         dbc.Col(dbc.NavbarBrand("Vivino Wine Visualization", className="ml-2",
            #                                 style={"color": "white", "fontSize": "20px"})),
                    

            #     ],
            #     align="center",
            #     no_gutters=True,

            # ),

            # href="https://www.vivino.com/",
        ),

        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),

    ],
    color="#2A385B",
)
# Multiple components can update everytime interval gets fired.
@app.callback([Output('finishButton', 'disabled'),
               Output('interval-component', 'interval')],
              [Input('interval-component', 'n_intervals'),])
def update_button(n):
    print(n)
    if(n==1):
        return [False,10000]


@app.callback(Output('label1', 'children'),
    [Input('interval-timer', 'n_intervals')])
def update_interval(n):
    return 'Time: ' + str(10-n) + ":00"



