# Import necessary libraries
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Load sales data from CSV
file_path = 'data/sales_data.csv'  # Adjust the path as needed
df_sales = pd.read_csv(file_path)

# Initialize Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("Sales Data Visualizer"),
    dcc.Graph(id='sales-line-chart')
])


# Callback function to update line chart based on user selection (if needed)
# For this specific task, assuming no interactivity is required beyond initial visualization
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('sales-line-chart', 'id')]  # Example input (not actually used in this case)
)
def update_chart(selected_value):
    # Filter data before and after January 15, 2021
    df_sales['Date'] = pd.to_datetime(df_sales['Date'])  # Ensure Date column is datetime type
    df_sales = df_sales.sort_values(by='Date')  # Sort by Date (assuming it's not already sorted)

    # Split data based on the date of price increase
    date_of_increase = pd.to_datetime('2021-01-15')
    df_before = df_sales[df_sales['Date'] < date_of_increase]
    df_after = df_sales[df_sales['Date'] >= date_of_increase]

    # Create line charts for before and after
    fig = px.line(df_sales, x='Date', y='Sales', title='Sales Trend over Time',
                  labels={'Date': 'Date', 'Sales': 'Sales'})

    # Highlight the point of price increase on the chart
    fig.add_vline(x=date_of_increase, line_dash="dash", line_color="red",
                  annotation_text="Price Increase", annotation_position="top right")

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
