from dash.dependencies import Input, State, Output
import dash_html_components as html
import dash_core_components as dcc


layout = html.Div([
    html.H3('Informatie kandidaat/Information candidate',id="consent_title"),
    
    html.P(" go to Qualtric form"),
    dcc.Link("Ready",  href='/visualizations',id="form_button",)

],id="mainConsent")

