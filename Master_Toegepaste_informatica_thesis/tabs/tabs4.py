import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from app import app
from interface_tabs import wine4
from interface_tabs.header import header
from interface_tabs.footer import footer



layout = html.Div([
    html.Div([header.navbar]),

    html.Div([
        dcc.Tabs(id="tabs4", value='tab-1', parent_className='custom-tabs', className='custom-tabs-container', children=[
            dcc.Tab(label='Wine', value='tab-1', className='custom-tab', selected_className='custom-tab--selected'),
            # dcc.Tab(label='Compare Wines', value='tab-2', className='custom-tab',selected_className='custom-tab--selected'),
            # dcc.Tab(label='Filter Attributes', value='tab-3', className='custom-tab', selected_className='custom-tab--selected'),
            # dcc.Tab(label='Data Table', value='tab-4', className='custom-tab',selected_className='custom-tab--selected')
            
        ])
        , html.Div(id="mainContainer4",style={"display": "flex", "flexDirection": "column"},),
    ]),
    html.Div([footer4.navbar]),

],)


@app.callback(Output('mainContainer4', 'children'),
              [Input('tabs4', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return wine4.layout


