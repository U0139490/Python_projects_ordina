
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


layout = html.Div([
    html.H3('Tutorial Video',id="consent_title"),
    
    html.Video(
            controls = True,
            id = 'movie_player',
            src = "assets/tutorial_video3.mp4",
            autoPlay=False
        ),
    html.Div(
    dbc.Button("Next",  href="https://kuleuven.eu.qualtrics.com/jfe/form/SV_dih8de0CTAcDfoh",id="tutorial_button")
    ,id="div_tutorial_button")
    # dcc.Link("Next", href="/form",id="tutorial_button",)

],id="mainTutorial")
