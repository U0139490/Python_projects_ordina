import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from app import app
from interface_tabs import wine2
from interface_tabs.header import header
from interface_tabs.footer import footer



layout = html.Div([
    html.Div([header2.navbar]),

    html.Div([
        dcc.Tabs(id="tabs2", value='tab-1', parent_className='custom-tabs', className='custom-tabs-container', children=[
            dcc.Tab(label='Wine', value='tab-1', className='custom-tab', selected_className='custom-tab--selected'),
            
        ])
        , html.Div(id="mainContainer2",style={"display": "flex", "flexDirection": "column"},),
    ]),
        html.Div([footer2.navbar]),

],)


@app.callback(Output('mainContainer2', 'children'),
              [Input('tabs2', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return wine2.layout


