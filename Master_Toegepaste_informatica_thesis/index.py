from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from app import server
from app import app
from intro_tabs import consent, tutorial
from tabs import *
import random


tabs_layout = [tabs.layout,tabs2.layout,tabs3.layout]
visited = [0,0,0]
reloadvis = [0,0,0]

s = random.sample(range(0,3), 3)

 
app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return consent.layout
    elif pathname == '/tutorial':
        return tutorial.layout
    elif pathname == '/visualizations':
        return tabs3.layout
    elif pathname == '/visualizations2':
        return tabs.layout  
    elif pathname == '/visualizations3':
        return tabs2.layout
    elif pathname == '/visualizations4':
        return tabs4.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server()