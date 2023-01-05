import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from app import app
from interface_tabs import wine, filter_attributes, data_table,compare_graph 
from interface_tabs.header import header
from interface_tabs.footer import footer

layout = html.Div([
    html.Div([header.navbar]),

    html.Div([
        dcc.Tabs(id="tabs", value='tab-1', parent_className='custom-tabs', className='custom-tabs-container', children=[
            dcc.Tab(label='Wine', value='tab-1', className='custom-tab', selected_className='custom-tab--selected'),
            # dcc.Tab(label='Compare Wines', value='tab-2', className='custom-tab',selected_className='custom-tab--selected'),
            # dcc.Tab(label='Filter Attributes', value='tab-3', className='custom-tab', selected_className='custom-tab--selected'),
            # dcc.Tab(label='Data Table', value='tab-4', className='custom-tab',selected_className='custom-tab--selected')
            
        ])
        , html.Div(id="mainContainer",style={"display": "flex", "flexDirection": "column"},),
    ]),
    html.Div([footer.navbar]),

],)


@app.callback(Output('mainContainer', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return wine.layout
    elif tab == 'tab-2':
        return compare_graph.layout
    elif tab == 'tab-3':
        return filter_attributes.layout
    elif tab == 'tab-4':
        return data_table.layout

