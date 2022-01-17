"""
    File name: main.py
    Author: Michael Hopkins
    Date created: 1/15/2020
    Date last modified: 1/16/2020
    Python Version: 3.10
"""

import dash
import plotly.express as px
from dash import dcc
from dash import html
from dash import dash_table
from MovingAverageChart import StockChart

# Nine days accounts for the time period minus the weekends
chart = StockChart('data.csv', 9)
df = chart.assembled_chart

app = dash.Dash(__name__)

# Setup line graph with multiple y values
line_graph = px.line(df, x='Date', y=['IBM 2DMovingAvg', 'AAPL 2DMovingAvg', 'MSFT 2DMovingAvg'])

app.layout = html.Div(children=[
    html.H1(children=''),

    html.Div(children='''
        Stock Closing Price and 2 Day Average for (IBM,AAPL,MSFT) over the period 2022.01.03 to 2022.01.13.
    '''),

    # convert dataframe to datatable
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),

    dcc.Graph(
        id='example-graph',
        figure=line_graph
    )])

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8050)
