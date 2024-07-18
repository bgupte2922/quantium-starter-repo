import pandas
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# the path to the formatted data file
DATA_PATH = "./formatted_data.csv"

# load in data
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# initialize dash
dash_app = Dash(__name__)

# define visualization function using Plotly Express
def generate_line_chart(selected_region):
    if selected_region == 'all':
        filtered_data = data # show all data
    else:
        filtered_data = data[data['region'] == selected_region]

    line_fig = px.line(filtered_data, x='date', y='sales', title='Pink Morsel Sales')
    return line_fig

# define app layout
dash_app.layout = html.Div([
    html.H1("Pink Morsel Visualizer", id="header"),

    dcc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all', # default value
        labelStyle={'display': 'inline-block', 'margin': '10px'}
    ),
    dcc.Graph(id="visualization"),
])

# define callback to update graph based on selected region
@dash_app.callback(
    Output('visualization', 'figure'),
    [Input('region-selector', 'value')]
)
def update_graph(selected_region):
    line_chart = generate_line_chart(selected_region)
    return line_chart

# add CSS styling
dash_app.css.append_css({
    'external-url': 'style.css'
})

# this is only true if the module is executed as the program entrypoint
if __name__ == '__main__':
    dash_app.run_server()

"""
To run above code OR Run the Dash App:
1. Open a terminal or command prompt.
2. Navigate to the directory where app.py is saved using the cd command.
3. Run the script: python app.py
4. Once the script is running, Open a web browser (like Chrome, Firefox, or Edge).
5. Enter the following URL in the address bar: http://127.0.0.1:8050 OR http://localhost:8050
6. The chart will be displayed on browser
7. To stop the Dash app and quit running the server, go back to your terminal where app.py is running.
8. Press CTRL+C to stop the server. This action will terminate the server and close the Dash app.
"""
