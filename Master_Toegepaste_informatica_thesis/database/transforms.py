import dash
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np



wine_csv = pd.read_csv("database/wines_review.csv", sep=';',
dtype={"wine": "string", "rating": np.float64,"language": "string",
                                                 "created_at": "string","note": "string",
                                                  "ratings_average": np.float64,"year": "string","country": "string",
                                                  "wine_type": "string", "region_name": "string",
                                                   "winery_name": "string","Sentiment": "string","Score": np.float64,}, index_col=0)

# wine_csv.info()

wine_csv2 = pd.read_csv("database/wine_data2.csv",low_memory=False, sep=';', index_col=0)

# dtype={"alcohol":np.float64, "category": "string","country": "string",
#                                                  "description": "string","designation": "string","rating": np.float64,
#                                                  "region": "string","title": "string","url": "string","varietal": "string",
#                                                  "winery": "string"},

wine_csv['created_at'] = pd.to_datetime(wine_csv['created_at'])


wine_csv_transform = wine_csv[['wine','rating','ratings_average','winery_name','created_at','note','wine_type','country','Sentiment']]

wineNames = wine_csv_transform['wine'].unique()

wines_names_rating = wine_csv_transform.groupby(['wine']).mean()['ratings_average'].reset_index()




