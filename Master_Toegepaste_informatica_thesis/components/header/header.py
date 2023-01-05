import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from app import app
import dash_html_components as html

from dash.dependencies import Input, Output, State


navbar = dbc.Navbar(
    [
        html.A(
            html.H3("Wine Dashboard",style={"color":"white"})
        ),
    ],
    color="#2A385B",
)




