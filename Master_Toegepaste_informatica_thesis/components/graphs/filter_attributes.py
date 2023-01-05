import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from app import app 
from database import transforms
import dash_bootstrap_components as dbc 
import dash_table
import pandas as pd


wine_csv_transform = transforms.wine_csv_transform

wine_csv2 = transforms.wine_csv2

countries = wine_csv2.groupby(['country']).mean()['rating'].sort_values(ascending=False).to_frame()
wineType = ["Red","White","Sparkling","Rose"]

options_answers = [{'label': "1", 'value': "1"},
                    {'label': "2", 'value': "2"},
                    {'label': "3", 'value': "3"},
                    {'label': "4", 'value': "4"},
                    {'label': "5", 'value': "5"}]
# html.Div(html.Img(src=app.get_asset_url('rating.png'))),  

layout = html.Div([
    html.H3("Tasks"),
    html.P(["Task 5: Do the following: "]),
     html.Ul([
                html.Li("Price: $0-$500"),
                html.Li("Alcohol: 10%-17%"),
                html.Li("Country: France, Itlay"),
                html.Li("Wine type: White, Red"),]),


    dbc.Row([ 
        dbc.Col(
        html.Div([
        html.Div([
            html.H2('Filter Wine Attributes'),
            html.H5('Price Slider')
            ,dcc.RangeSlider(id='price-slider'
                            ,min = 0
                            ,max= 2500
                            , marks = {0: '$0',
                                        500: '$500',
                                        1000: '$1000',
                                        1500: '$1500',
                                        2000: '$2000',
                                        2500: '$2500',
                                       }
                            , value = [0,50]
                            )
                        
                            ]),
         html.Div([html.H5('Alcohol Percentage')
            ,dcc.RangeSlider(id='alcohol-slider'
                            ,min = 5
                            ,max= 17
                            , marks = {5: '5',
                                        6: '6',
                                        7: '7',
                                        8: '8',
                                        9: '9',
                                        10: '10',
                                        11: '11',
                                        12: '12',
                                        13: '13',
                                        14: '14',
                                        15: '15',
                                        16: '16',
                                        17: '17',
                                       }
                            , value = [15,17]
                            )
                        
                            ]),
        html.Div([html.P(),
        html.H5('Country'), 
        dcc.Dropdown(id = 'country-drop',
                    options=[{'label': i, 'value': i} for i in list(countries.index)],
                    value=["France","Italy"],
                    multi=True
                    )]),
        html.Div([html.P(),
        html.H5('Wine Types'), 
        dcc.Dropdown(id = 'wineType-drop',
                    options=[{'label': i, 'value': i} for i in list(wineType)],
                    value=["White","Red"],
                    multi=True
                    )]) 
                    
        ],style={'color':'black'}),className='pretty_container four columns',id="cross-filter-options",),

        dbc.Col( html.Div( dcc.Graph(id="scatterplot", )),width=4,className='pretty_container',),    
        dbc.Col( html.Div(dcc.Graph(id="boxplot", )),width=4,className='pretty_container')
        
        ]),
        
    dbc.Row([ 
        dbc.Col(html.Div(dcc.Graph(id="heatmap")),className='pretty_container',style={"width":"calc(100% - 30px)"}), 
     ]),

])


@app.callback([Output("heatmap", "figure"),Output("scatterplot", "figure"),Output("boxplot", "figure")],
      [Input("country-drop", "value"),
      Input("wineType-drop", "value"),
      Input('price-slider', 'value'),
      Input('alcohol-slider', 'value')])

def update_figure(country, winetype,prices,alcohol):
    dff = wine_csv2.groupby(['title','country','category','price','alcohol']).mean()['rating'].reset_index()
    dff = dff.loc[dff['country'].isin(country)]

    lowP = prices[0]
    highP = prices[1]
   
    lowAl = alcohol[0]
    highAl = alcohol[1]
   
    if country is None:
        province = []
    if winetype is None:
        winetype = []


    if len(country) > 0 and len(winetype) > 0:
        dff = dff.loc[dff['country'].isin(country) & dff['category'].isin(winetype) & (dff['price'] >= lowP) & (dff['price'] <= highP)
        & (dff['alcohol'] >= lowAl) & (dff['alcohol'] <= highAl)]
   
    elif len(country) > 0 and len(winetype) == 0:
        dff = dff.loc[dff['country'].isin(country) & (dff['price'] >= lowP) & (dff['price'] <= highP)
         & (dff['alcohol'] >= lowAl) & (dff['alcohol'] <= highAl)]

    else:
        dff

    # dff_heatmap = dff.sort_values(by=['rating'],ascending=False).head()
    # print(dff_heatmap)
    graph_heatmap = go.Heatmap(z=dff['rating']
                , x=dff['title']
                , y=dff['country']
                , hoverongaps = True
                , colorscale='RdBu', colorbar={"title": "Average Rating", 'x':-.17},zmin=1,zmax=5, showscale=True)
    layout_heatmap =dict (  
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                xaxis= dict(),
                yaxis= {"automargin": True, 'side': "right"},
                margin= {"t": 20, "l": 30, "r": 100,    }
                )
    #Scatterplot
    # print(np.corrcoef(dff['rating'], dff['price']))
    graph_scatterplot = go.Scattergl(x = dff['rating']
                        , y = dff['price']
                        , mode='markers'
                        , text=dff["title"]
                        , opacity=0.7
                        , marker={
                                'size': 8
                                , 'line': {'width': 0.5, 'color': 'white'}
                                })    
                        
    layout_scatterplot = dict(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',

                    xaxis={'type': 'log', 'title': 'Rating'},
                    yaxis={'title': 'Price'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
    #Boxplot
    graphs_box = []
    colors = ""
    for i in winetype:
        if i =="White":
            colors = "#005AB5"
        if i == "Red":
            colors = "#DC3220"
        if i == "Sparkling":
            colors = "#FFC20A"
        if i == "Rose":
            colors = "#4B0092"
        avgRating_wineType =  dff.loc[dff['category'].isin([i])]
        graph_boxplot = go.Box( y=avgRating_wineType['rating'],
                        name = i,
                        marker = dict(
                        color = colors,
                        opacity=1,)
                    )
        graphs_box.append(graph_boxplot)
    layout_boxplot = dict(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',

                    xaxis= dict(title='Wine Type',),
                    yaxis=dict(title='Rating',range=[0.2,6]),
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest')


    return {
            "data": [graph_heatmap],
            "layout":layout_heatmap 
            },{
            "data": [graph_scatterplot],
            "layout":layout_scatterplot 
            }, {
            "data": graphs_box,
            "layout":layout_boxplot 
        }
