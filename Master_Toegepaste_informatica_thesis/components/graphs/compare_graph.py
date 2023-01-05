import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, State, Output
from app import app
from database import transforms
import plotly.graph_objects as go
import pandas as pd
import random
import numpy as np
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate

wine_csv_transform = transforms.wine_csv_transform

wineNames = transforms.wineNames

def get_random_hex():
    random_number = random.randint(0, 16777215)

    # convert to hexadecimal
    hex_number = str(hex(random_number))

    # remove 0x and prepend '#'
    return '#' + hex_number[2:]

start_options = [{'label':'mandorla Shiraz 2011', 'value':'mandorla Shiraz 2011'},
                {'label':'mandorla Shiraz 2010', 'value':'mandorla Shiraz 2010'},
                {'label':'Small Town Pinot Noir 2013', 'value':'Small Town Pinot Noir 2013'}]


options_answers = [{'label': "1", 'value': "1"},
                    {'label': "2", 'value': "2"},
                    {'label': "3", 'value': "3"},
                    {'label': "4", 'value': "4"},
                    {'label': "5", 'value': "5"}]
layout = html.Div([
    html.H3("Tasks"),
    html.P(["Task 3: Compare the wines ", html.Span("Dolcetto d'Alba 2013",style={"fontWeight":"bold"})," and ", html.Span("Reserve Zinfandel 2013",style={"fontWeight":"bold"})," and write down ", html.Span("how many reviews",style={"fontWeight":"bold"}), " each wine has."]),
    html.P(["Task 4: For the same wines in task 3, write down ", html.Span("the name of the country",style={"fontWeight":"bold"})," that their from and ", html.Span("the average rating",style={"fontWeight":"bold"}),"  of the wines in that country."]),

    dbc.Row(
    [ 
        dbc.Col( html.Div(
                    [
                        html.H2('Compare wines'),

                        html.Label([ dcc.Dropdown(id="wines_compare",
                        options=start_options,
                        value=['mandorla Shiraz 2011','mandorla Shiraz 2010','Small Town Pinot Noir 2013'],
                        multi=True,
                        style={"padding":"5px","marginTop": "20px",'width': '250px'})]),
                      
                        dbc.Button("Compare", id="compare-button", n_clicks=0,block=True,color="primary", className="ml-2",
                        style={"marginTop": "20px"}),
                       

               
            ], className="pretty_container",
                    id="searchWineDiv_tab1",),),
        dbc.Col( html.Div( dcc.Graph(id="graph_compare_barchart", )),width=4,className='pretty_container',),    
        dbc.Col( html.Div(dcc.Graph(id="graph_compare_boxplot", )),width=4,className='pretty_container')
        
        ]),
     dbc.Row([ 
        dbc.Col([
            html.Div([],id="wines_compare_countries",style ={"float":"left"}),
            html.Div(dcc.Graph(id="graph_compare"))],className='pretty_container',style={"overflow": "hidden","width":"calc(100% - 30px)"}), 
     ]),


])



@app.callback([Output("graph_compare", "figure"),
               Output("graph_compare_barchart", "figure"),
               Output("graph_compare_boxplot", "figure")],
              [Input("compare-button", "n_clicks")],
              [State("wines_compare", "value")])
def compare_fig(n_clicks, winesList):
    c = 0
    boxplots_graphs = []
    if len(winesList) != 0:
        data = []
        colors=["#465EAC","#958300","#8C8889","#D0CECF","#E5D076"]

        dff = wine_csv_transform.loc[wine_csv_transform['wine'].isin(winesList)]
        countries = dff.groupby(['country']).mean()['rating'].reset_index()

        data_specific_countries = wine_csv_transform.loc[wine_csv_transform['country'].isin(list(countries["country"]))]
        map_data = data_specific_countries.groupby(['country']).mean()['rating'].reset_index()

        map_graph = go.Choropleth(
            locations = map_data['country'],
            locationmode = 'country names',
            autocolorscale = False,
            colorscale = 'RdBu',
            text= map_data['country'],
            z=map_data['rating'].round(1),
            marker = dict(line = dict(color = 'rgb(255,255,255)')
            
            ),colorbar = {'title':'Average Rating'},zmin=1,zmax=5, showscale=True),


        layout_map = dict(
            title="Average Rating Of wines In Country",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',    
            geo = dict(scope='world'))




        # dff = dff.sort_values(by=['created_at'])
        # scatterplot_graph = go.Scatter(x=list(dff['created_at'].dt.strftime('%Y')),
        #                     y=list(dff['rating']),
        #                     mode='markers',
        #                     text=dff['note'],
        #                     marker=go.scatter.Marker(
        #                         size=np.where(dff['rating'] > 3.0, 20, 10),
        #                         color=  colors,
        #                         opacity=0.6,
        #                     ))
        # data.append(scatterplot_graph)
        # layout = dict(
        #         title="Review Year VS Rating",
        #         paper_bgcolor='rgba(0,0,0,0)',
        #         plot_bgcolor='rgba(0,0,0,0)',
        #         xaxis = dict(
        #         title = "Year"),
        #         yaxis=dict(title='Rating'),
        #         autosize=False, )
        for i in winesList:
            specific_wine = wine_csv_transform.loc[ wine_csv_transform['wine']== i]

            graph_boxplot = go.Box( y=specific_wine['rating'],
                            name = i,
                            marker = dict(
                            color =  colors[c],
                            opacity=1,)
                        )          
            boxplots_graphs.append(graph_boxplot)
            c = c + 1

        layout_graph_boxplot = dict(
                        paper_bgcolor='rgba(0,0,0,0)',
                         plot_bgcolor='rgba(0,0,0,0)',
                        xaxis= dict(title='Wines',),
                        yaxis=dict(title='Rating',range=[0.2,6]),
                        margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest')


        amount_review= []
        
        for i in winesList:
            specific_wine = wine_csv_transform.loc[ wine_csv_transform['wine']== i]
            amount = len(specific_wine.index)
            amount_review.append(amount)
        

        amount_review_bar = go.Bar(
        x=winesList,
        y=amount_review,
        name='Amount Reviews',
        orientation='v',
        marker=dict(
            color=colors,
            line=dict(color=colors, width=3)
        ))
          
        layout2 = dict(
            title="Amount Reviews",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis = dict(
            title = "wines",
            tickangle = 45,
            title_font = {"size": 20},
            title_standoff = 25),
            yaxis=dict(title='Reviews'),
            autosize=False, )

      

        return {
                "data": map_graph,
                "layout": layout_map,
            },{
                "data": [amount_review_bar],
                "layout": layout2,
            },{
                "data": boxplots_graphs,
                "layout":layout_graph_boxplot 
            }


    layout4 = dict(title="Date wines", )
    return {
        "data": [],
        "layout": layout4,
    },{
        "data": [],
        "layout": layout4,
    },{
        "data": [],
        "layout": layout4,
    }


@app.callback(Output("wines_compare_countries", "children"),
              [Input("compare-button", "n_clicks")],
              [State("wines_compare", "value")])
def compare_fig(n_clicks, winesList):
    divs = []

    if len(winesList) != 0:
        dff = wine_csv_transform.loc[wine_csv_transform['wine'].isin(winesList)]
        for i in winesList:
            specific_wine = (dff.loc[ dff['wine']== i])
            data_wine = specific_wine.groupby(['wine',"country"]).mean()['rating'].reset_index()
            divs.append(html.Div([html.H5(data_wine['wine']),html.Div(html.P("country: " + data_wine['country']))],id="wells"))
    
    return divs
        

@app.callback(Output("wines_compare", "options"),
    [Input("wines_compare", "search_value")],
    [State("wines_compare", "value")],
)
def update_multi_options(search_value, value):
    if not search_value:
        raise PreventUpdate
    if len(value) < 5:
        options = list(filter(lambda x: x.lower().startswith(search_value.lower()), wineNames)) 
        options = options[:5]
        options = options + value
        options = [{'label':opt, 'value':opt} for opt in options]
        return  options

    options = value
    options = [{'label':opt, 'value':opt} for opt in options]
    return  options


   
