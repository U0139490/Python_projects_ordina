import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from app import app
from interface_tabs import wine3
from interface_tabs.header import header
from interface_tabs.footer import footer



layout = html.Div([
    html.Div([header3.navbar]),

    html.Div([
        dcc.Tabs(id="tabs3", value='tab-1', parent_className='custom-tabs', className='custom-tabs-container', children=[
            dcc.Tab(label='Wine', value='tab-1', className='custom-tab', selected_className='custom-tab--selected'),
  
            
        ])
        , html.Div(id="mainContainer3",style={"display": "flex", "flexDirection": "column"},),
    ]),
    html.Div([footer3.navbar]),

],)


@app.callback(Output('mainContainer3', 'children'),
              [Input('tabs3', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return wine3.layout


