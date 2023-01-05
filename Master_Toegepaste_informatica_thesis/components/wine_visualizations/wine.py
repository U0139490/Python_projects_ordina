import dash
import random
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, State, Output
from app import app
from database import transforms
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import urllib
#import requests
import seaborn as sns 
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from dash.exceptions import PreventUpdate
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.corpus import stopwords
from nltk import word_tokenize
import time


wine_csv_transform = transforms.wine_csv_transform

wineNames = transforms.wineNames

def fig_to_uri(in_fig, close_all=True, **save_args):
    # type: (plt.Figure) -> str
    """
    Save a figure as a URI
    :param in_fig:
    :return:
    """
    out_img = BytesIO()
    in_fig.savefig(out_img, format='png', **save_args,transparent=True)
    if close_all:
        in_fig.clf()
        plt.close('all')
    out_img.seek(0)  # rewind file
    encoded = base64.b64encode(out_img.read()).decode("ascii").replace("\n", "")
    return "data:image/png;base64,{}".format(encoded)

def transform_format(val):
    if val == 0:
        return 255
    else:
        return val



# set seaborn style 
sns.set(style="whitegrid")

stopwords = set(stopwords.words('english'))
# Detokenizer combines tokenized elements
detokenizer = TreebankWordDetokenizer()

def clean_description(desc):
    desc = word_tokenize(desc.lower())
    desc = [token for token in desc if token not in stopwords and token.isalpha()]
    return detokenizer.detokenize(desc)

options_answers = [{'label': "1", 'value': "1"},
                    {'label': "2", 'value': "2"},
                    {'label': "3", 'value': "3"},
                    {'label': "4", 'value': "4"},
                    {'label': "5", 'value': "5"}]

def negative_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):

    return "hsl({}, {}%, {}%)".format(6, 75, 49)

def positive_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):

    return "hsl({}, {}%, {}%)".format(210, 100, 35)

def neutral_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):

    return "hsl({}, {}%, {}%)".format(45, 100, 52)

characteristics = ["dry","smooth","fruit","fruity","soft","red","white","rose","cheap","price","oak",'wood',"quality"
                            ,"bold","light","sweet","acidic","cheese","cream","oil","pepper","spicy","mint","savory","butter","vanilla","toffee",
                            "raspberries","juicy","heavy","balanced","fruitiness","acidity","drinkability","finesse","fizziness","flavors","boozy",
                            "rich","sweetness","old","oaky","polished","young","silky","freshness","bright","cherry","elegant","fruits","drinkable",
                            "structure","balance","color","dark","enjoyable","mild","aftertaste","bitter","delicate","berries","fresh","floral","colored",
                            "savoury","simple","ripe","blueberries","tannins","textural","firm","plum","vivid","chocolate","peppery","raisin","warm",
                            "slender","ruby","cranberry","aromas","walnuts","breathe","honning","alcohol","taste","apple","citrus","dessert",
                            "dried","tannin","almond","vibrant","prunes","affordable","grapes","undrinkable","intensity","orange","age",
                            "strawberry","aromatic","flat"]
# Create app layout
layout = html.Div(
    [

        html.Details([
        html.Summary('Click here to open the Task'),
        html.Div([
            html.P(["Search for ", html.Span("Zinfandel 2010",style={"fontWeight":"bold"})," and write down ", html.Span("the top 3 ",style={"fontWeight":"bold"}), "most frequent wine characteristics looking at visualizations for:"]),      
            html.Ul([
                html.Li("Negative reviews"),
                html.Li("Neutral reviews"),
                html.Li("Positive reviews")]),
        
        html.P("Example for task:",style={"padding-left":"5px","fontStyle": "italic","fontWeight":"bold"}),
        html.Ul([
            html.Li("Negative reviews: dry, sweet, acidity"),
            html.Li("Neutral reviews: fruity, light, color"),
            html.Li("Positive reviews: soft, fresh, spicy")],style={"margin-left":"5px","fontStyle": "italic"}),

        ])
        ]),
   
        # html.P(["Task 2: Search for ", html.Span("Indian Wells Riesling",style={"fontWeight":"bold"}), " and write down the ", html.Span("top 3",style={"fontWeight":"bold"}), " most frequent words used by the reviewers."]),

        # html.H3("Question"),
        # html.P("Question 1: What's been the most useful visualization component for the given tasks?"),
        # html.P("Question 2: What's been the least useful visualization component for the given tasks?"),
        # html.P("Question 3: Do you have further suggestions for improvement?"),


  
        dcc.Store(id="aggregate_data"),
        # empty Div to trigger javascript file for graph resizing
        html.Div(id="output-clientside"),
    
       

        html.Div(
            [
            #     html.Div(
            #         [
            #             html.H2('Search Wine'),

            #             html.Label([ dcc.Dropdown(id="wine_input",
            #             options=[{'label':'Brunus Rose 2013', 'value':'Brunus Rose 2013'}],
            #             value='Brunus Rose 2013'
            #             ,style={"marginTop": "20px",'width': '250px'})]),
                      
            #             dbc.Button("Search", id="submit-button", n_clicks=0,block=True,color="primary", className="ml-2",
            #             style={"marginTop": "20px"}),
                       

               
            # ], className="pretty_container four columns",
            #         id="searchWineDiv_tab1",),

                html.Div(
                    [

                        html.Div(
                            [
                                  html.Div(
                                        [
                                    html.H2('Search Wine'),

                                    html.Label([ 
                                        
                                    dcc.Dropdown(id="wine_input",
                                    options=[{'label':'Brunus Rose 2013', 'value':'Brunus Rose 2013'},
                                            {'label':'Zinfandel 2010', 'value':'Zinfandel 2010'},
                                            {'label':"Dolcetto d'Alba 2013", 'value':"Dolcetto d'Alba 2013"}],
                                    value='Brunus Rose 2013'
                                    ,style={"marginTop": "20px",'width': '250px'}),
                                        
                                    dcc.Loading(
                                        id="loading-1",
                                        type="dot",
                                        children=html.Div(id="loading-output-1"),
                                        color="#AE1832",
                                        style={"paddingTop": "50px"}
                                    ),
                                    
                                    
                                    
                                    ]),
                                
                                    dbc.Button("Search", id="submit-button", n_clicks=0,block=True,color="primary", className="ml-2",
                                    style={"marginTop": "20px"}),
                                ], className="mini_container",),
                                html.Div(
                                    [ html.H5('Average Rating'),html.H6(id="well_text"),  html.Div(id='output_averageRating',style={"fontSize":"20px","margin":"auto","margin-top":"15%","textAlign":"center"}),
                          
                
                                    ],
                                    id="wells",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H5('Winery'),html.H6(id="gasText"),  html.Div(id='output_wineryName',style={"fontSize":"20px","margin":"auto","margin-top":"15%","textAlign":"center"})],
                                    id="gas",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H5('Country'), html.H6(id="oilText"), html.Div(id='output_countryName',style={"fontSize":"20px","margin":"auto","margin-top":"15%","textAlign":"center"})],
                                    id="oil",
                                    className="mini_container",
                                ),
                              
                            ],
                            id="info-container",
                            className="row container-display",
                        ),
               

                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display", 
        ),

        html.Div(
                [
                        html.Div(
                        [dcc.Graph(id="graph1_tab1")],
                        className="pretty_container",id="graph1_tab1_div"),

                        html.Div(
                        [dcc.Graph(id="graph2_tab1")],
                        className="pretty_container",id="graph2_tab1_div"),
                
                ],
                className="row flex-display"),
        # html.Div([                
        #     html.H2('SECTION 1',style={"color":"white", "fontWeight":"bold","padding":"5px"}),
        html.Div(
            [

                 html.Div(
                    [ html.Div(html.Img(id = 'wordcloud_negative', src = ''),)],
                    className="pretty_container five columns",id="div_barchar_sentiment"
                ),
                 html.Div(
                    [ html.Div(html.Img(id = 'wordcloud_neutral', src = ''),)],
                    className="pretty_container five columns",id="div_barchar_sentiment"
                ),
                html.Div(
                    [ html.Div(html.Img(id = 'wordcloud_positive', src = ''),)],
                    className="pretty_container five columns",id="div_barchar_sentiment"
                ),
               
            ],
            className="row flex-display", ),
        
    ])


@app.callback(Output("graph1_tab1", "figure"),
             [Input("submit-button", "n_clicks")],
              [State("wine_input", "value")])
def update_fig1(n_clicks, input_value):
    if input_value is not None:
        specific_wine = (wine_csv_transform.loc[ wine_csv_transform['wine']== input_value])
        ratings =[]
        for r in list(specific_wine['rating']):
            if(r==1):
                ratings.append(-2)
            if(r==1.5):
                ratings.append(-1.5)
            if(r==2):
                ratings.append(-0.5)
            if(r==2.5):
                ratings.append(0)
            if(r==3):
                ratings.append(0.5)
            if(r==3.5):
                ratings.append(1.5)
            if(r==4):
                ratings.append(2)
            if(r==4.5):
                ratings.append(2.5)
            if(r==5):
                ratings.append(3)
        lenght_review =[]
        for r in list(specific_wine['note']):
            if (len(r)<15):
                lenght_review.append(-3)
            if (15 <= len(r) < 20):
                lenght_review.append(-2)
            if (20 <= len(r) < 25):
                lenght_review.append(-1)
            if (25 <= len(r) < 30):
                lenght_review.append(0)
            if (30 <= len(r) < 35):
                lenght_review.append(1)
            if (35 <= len(r) < 40):
                lenght_review.append(2)
            if (len(r)>40):
                lenght_review.append(3)

        # ratings_string = list(map(str,list(specific_wine['rating']))) 
        wine_graph = go.Scatter(x=ratings,
                                y=lenght_review,
                                name="Close",
                                line=dict(color="blue"),
                                mode='markers',
                                hovertemplate =
                                    # '<i>Price</i>: $%{y:.2f}'+
                                    '<b>Rating: %{text}</b>'+
                                    '<br><b>Review</b>: '+ specific_wine['note'] +'<br>',
                                text =  specific_wine['rating'],
                                marker=go.scatter.Marker(
                                    size=np.where(specific_wine['rating'] > 3.0, 20, 10),
                                    color=  [ '#005AB5' if v == "positive" else '#FFC20A' if v == "neutral" else '#DC3220' for v in specific_wine["Sentiment"] ],
                                    opacity=1,
                                ))
        data = [wine_graph]
        layout1 = dict(
            title="Scatterplot: Reviews",
             paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            hovermode='closest',
            xaxis= dict(
                title='Rating',
                range=[-3,4],
                mirror= "allticks",
                 side= 'bottom', 
                autorange=True,
                showgrid=False,
                ticks='',
                showticklabels=False),

            yaxis = dict(
                title='Passive-Assertive Review',
                range=[-4,4],  
                mirror= "allticks",
                 side= 'left',
                autorange=True,
                showgrid=False,
                ticks='',
                showticklabels=False              
                ),  
              
            showlegend= False,          
            autosize=False, )
        

        return {
                "data": data,
                "layout": layout1,

            }
        
    empty_layout =dict()
    return {
        "data": [],
        "layout": empty_layout,   

    }


@app.callback(Output("graph2_tab1", "figure"),
              [Input("submit-button", "n_clicks")],
              [State("wine_input", "value")])
def update_fig2(n_clicks, input_value):
    if input_value is not None:
        specific_wine = (wine_csv_transform.loc[ wine_csv_transform['wine']== input_value])
        specific_wine = specific_wine.sort_values(by=['created_at'])

        labels = ['Positive', 'Negative','Neutral']
        values = []
        
        amount_pos = specific_wine.query('Sentiment == "positive"').Sentiment.count()
        amount_neg = specific_wine.query('Sentiment == "negative"').Sentiment.count()
        amount_neutral = specific_wine.query('Sentiment == "neutral"').Sentiment.count()
        values.append(amount_pos)
        values.append(amount_neg)
        values.append(amount_neutral)
        colors = ['#005AB5', '#DC3220','#FFC20A']

        pie_chart = go.Pie(labels=labels, values=values, 
                            marker=dict(colors=colors, 
                            line=dict(color='#0C0F0A', width=2)))
        data2 = [pie_chart]
        layout2 = dict(

            title='Sentiment Percentage Of Reviews',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            autosize=False, )
        

        return  {
                "data": data2,
                "layout": layout2,
            }
    empty_layout =dict()
    return {
        "data": [],
        "layout": empty_layout,   

    }


@app.callback([Output("wordcloud_negative", "src"),
                Output("wordcloud_positive", "src"),
                Output("wordcloud_neutral", "src")],
              [Input("submit-button", "n_clicks")],
              [State("wine_input", "value")])
def update_wordclouds(n_clicks, input_value):
    if input_value is not None:
        specific_wine = (wine_csv_transform.loc[ wine_csv_transform['wine']== input_value])
        negative_reviews = (specific_wine.loc[ specific_wine['Sentiment']== "negative"])
        positive_reviews = (specific_wine.loc[ specific_wine['Sentiment']== "positive"])
        neutral_reviews = (specific_wine.loc[ specific_wine['Sentiment']== "neutral"])
    

        # mask = np.array(Image.open(requests.get('http://www.clker.com/cliparts/O/i/x/Y/q/P/yellow-house-hi.png', stream=True).raw))
        # https://www.dlf.pt/png/big/21/215164_wine-glass-png.png
        # wine_mask =  np.array(Image.open(requests.get('http://www.clker.com/cliparts/O/i/x/Y/q/P/yellow-house-hi.png', stream=True).raw))

        # transformed_wine_mask = np.ndarray((wine_mask.shape[0],wine_mask.shape[1]), np.int32)
        # for i in range(len(wine_mask)):
        #     transformed_wine_mask[i] = list(map(transform_format, wine_mask[i]))
        if (len(negative_reviews) != 0):
            negative_reviews_des = negative_reviews["note"].apply(clean_description)
            word_occurrence_negative = negative_reviews_des.str.split(expand=True).stack().value_counts()
            word_occurrence_negative = word_occurrence_negative.loc[word_occurrence_negative.index.isin(characteristics)]
            if (len(word_occurrence_negative) != 0):
                negative_wordcloud = WordCloud(
                        background_color = '#f9f9f9',
                        color_func=negative_color_func,
                        width = 400,
                        height = 360, max_words=20,).generate(' '.join(word_occurrence_negative.index))
            else:
                negative_wordcloud = WordCloud(stopwords = set(STOPWORDS),
                    background_color = '#f9f9f9',
                    color_func=negative_color_func,
                        width = 400,
                    height = 360, max_words=2,).generate("NO NEGATIVE")
        else:
            negative_wordcloud = WordCloud(stopwords = set(STOPWORDS),
                    background_color = '#f9f9f9',
                    color_func=negative_color_func,
                        width = 400,
                    height = 360, max_words=2,).generate("NO NEGATIVE")
        if (len(positive_reviews) != 0):
            positive_reviews_des = positive_reviews["note"].apply(clean_description)
            word_occurrence_positive = positive_reviews_des.str.split(expand=True).stack().value_counts()
            word_occurrence_positive = word_occurrence_positive.loc[word_occurrence_positive.index.isin(characteristics)]
            if (len(word_occurrence_positive) != 0):
                positive_wordcloud = WordCloud(
                        background_color = '#f9f9f9',
                        color_func=positive_color_func,
                        width = 400,
                        height = 360, max_words=20,).generate(' '.join(word_occurrence_positive.index))
            else:
                positive_wordcloud = WordCloud(stopwords = set(STOPWORDS),
                    background_color = '#f9f9f9',
                    color_func=positive_color_func,
                    width = 400,
                    height = 360, max_words=2,).generate("NO POSITIVE")
        else:
            positive_wordcloud = WordCloud(stopwords = set(STOPWORDS),
                    background_color = '#f9f9f9',
                    color_func=positive_color_func,
                    width = 400,
                    height = 360, max_words=2,).generate("NO POSITIVE")
        
        if (len(neutral_reviews) != 0):   
            neutral_reviews_des = neutral_reviews["note"].apply(clean_description)
            word_occurrence_neutral = neutral_reviews_des.str.split(expand=True).stack().value_counts()
            word_occurrence_neutral = word_occurrence_neutral.loc[word_occurrence_neutral.index.isin(characteristics)]
            if (len(word_occurrence_neutral) != 0):   
                neutral_wordcloud = WordCloud(
                        background_color = '#f9f9f9',
                        color_func=neutral_color_func,
                        width = 400,
                        height = 360, max_words=20,).generate(' '.join(word_occurrence_neutral.index))
            else:
                neutral_wordcloud = WordCloud(stopwords = set(STOPWORDS),
                    background_color = '#f9f9f9',
                    color_func=neutral_color_func,
                    width = 400,
                    height = 360, max_words=2,).generate("NO NEUTRAL")
        else:
            neutral_wordcloud = WordCloud(stopwords = set(STOPWORDS),
                    background_color = '#f9f9f9',
                    color_func=neutral_color_func,
                    width = 400,
                    height = 360, max_words=2,).generate("NO NEUTRAL")

#  mask=wine_mask,contour_width=3, contour_color='firebrick'
        fig, ax1 = plt.subplots(figsize = (3.6,3.6),facecolor = 'black', edgecolor='blue')
        bg_color = 'black'
        ax1.patch.set_facecolor(bg_color)
        plt.imshow(negative_wordcloud) # image show
        plt.axis('off') # to off the axis of x and y
        plt.title("Word Cloud: Negative Reviews", color='black', fontsize=10, horizontalalignment='center')
        plt.savefig('World_Cloud_negative.png',transparent=True)

        fig2, ax2 = plt.subplots(figsize = (3.6,3.6),facecolor = 'black', edgecolor='blue')
        ax2.patch.set_facecolor(bg_color)
        plt.imshow(positive_wordcloud) # image show
        plt.axis('off') # to off the axis of x and y
        plt.title("Word Cloud: Positive Reviews", color='black', fontsize=10, horizontalalignment='center')
        plt.savefig('World_Cloud_positive.png',transparent=True)

        fig3, ax3 = plt.subplots(figsize = (3.6,3.6),facecolor = 'black', edgecolor='blue')
        ax3.patch.set_facecolor(bg_color)
        plt.imshow(neutral_wordcloud) # image show
        plt.axis('off') # to off the axis of x and y
        plt.title("Word Cloud: Neutral Reviews", color='black', fontsize=10, horizontalalignment='center')
        plt.savefig('World_Cloud_neutral.png',transparent=True)

        out_url = fig_to_uri(fig)
        out_url2 = fig_to_uri(fig2)
        out_url3 = fig_to_uri(fig3)

        return out_url,out_url2,out_url3




@app.callback([Output('output_averageRating', 'children'),
                Output('output_wineryName', 'children'),
                Output('output_countryName', 'children')],
             [Input("submit-button", "n_clicks")],
              [State("wine_input", "value")])
def update_output(n_clicks, input_value):
    divs1=[]
    divs2=[]
    divs3=[]

    if input_value is not None:
        specific_wine = (wine_csv_transform.loc[ wine_csv_transform['wine']== input_value])
        dff1 = specific_wine.groupby(['wine']).mean()['rating'].reset_index()
        dff2 = specific_wine.groupby(['winery_name']).mean()['rating'].reset_index()
        dff3 = specific_wine.groupby(['country']).mean()['rating'].reset_index()

        if(dff1['rating'].round(0).iloc[0]==1.0):
           divs1.append( html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star")),
           divs1.append(html.Span(className="fa fa-star")),
           divs1.append(html.Span(className="fa fa-star")),
           divs1.append(html.Span(className="fa fa-star")),
        if(dff1['rating'].round(0).iloc[0]==2.0):
           divs1.append( html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star")),
           divs1.append(html.Span(className="fa fa-star")),
           divs1.append(html.Span(className="fa fa-star")),
        if(dff1['rating'].round(0).iloc[0]==3.0):
           divs1.append( html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star")),
           divs1.append(html.Span(className="fa fa-star")),
        if(dff1['rating'].round(0).iloc[0]==4.0):
           divs1.append( html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star"))
        if(dff1['rating'].round(0).iloc[0]==5.0):
           divs1.append( html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star checked")),
           divs1.append(html.Span(className="fa fa-star checked")),

        divs2.append(html.P(dff2['winery_name'].iloc[0]))
        divs3.append(html.P(dff3['country'].iloc[0]))


    return divs1,divs2,divs3

