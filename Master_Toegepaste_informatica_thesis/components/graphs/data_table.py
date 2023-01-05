import dash
import dash_table
import dash_html_components as html
from database import transforms


wines_names_rating = transforms.wines_names_rating




def generate_table(data_frame):
    return dash_table.DataTable(
        data=data_frame.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in data_frame.columns],
        style_cell={'textAlign': 'left'},
        style_cell_conditional=[
            {
                'if': {'column_id': 'wine'},
                'textAlign': 'center'
            }
        ],
        style_table={
            'maxHeight': '500px',
            'overflowY': 'scroll',
        },
    )


layout = html.Div([
    html.Div(children=[
        generate_table(wines_names_rating)
    ], style={"padding": "25px"})
])
