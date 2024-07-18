import pandas
from dash import Dash, html, dcc, Input, Output

from plotly.express import line

# the path to the formatted data file
DATA_PATH = "./formatted_data.csv"
COLORS = {
    "primary": "#FEDBFF",
    "secondary": "#D598EB",
    "font": "#522A61"
}

# load in data
data = pandas.read_csv(DATA_PATH)
data = data.sort_values(by="date")

# initialize dash
dash_app = Dash(__name__)

# create the visualization
def generate_figure(chart_data):
    line_chart = line(chart_data, x="date", y="sales", title="Pink Morsel Sales")
    line_chart.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )
    return line_chart


visualization = dcc.Graph(
    id="visualization",
    figure=generate_figure(data)
)

# create the header
header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)

# region picker
region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)
region_picker_wrapper = html.Div(
    [
        region_picker
    ],
    style={
        "font-size": "150%"
    }
)


# define the region picker callback
@dash_app.callback(
    Output(visualization, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    # filter the dataset
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]

    # generate a new line chart with the filtered data
    figure = generate_figure(trimmed_data)
    return figure


# define the app layout
dash_app.layout = html.Div(
    [
        header,
        visualization,
        region_picker_wrapper
    ],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "border-radius": "20px"
    }
)

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
