import dash
from dash import html
from dash.testing.application_runners import import_app
from dash.testing.base import DashDuo

# Fixture to start Dash app for testing
def get_app():
    app = import_app("app")
    return app

# Test cases
def test_header_present(dash_duo: DashDuo):
    app = get_app()
    dash_duo.start_server(app)

    # Assert header is present
    header = dash_duo.find_element("#header-id")
    assert header.text == "Your Header Text"

    dash_duo.stop_server()

def test_visualization_present(dash_duo: DashDuo):
    app = get_app()
    dash_duo.start_server(app)

    # Assert visualization component is present
    visualization = dash_duo.find_element("#visualization-id")
    assert visualization.exists()

    dash_duo.stop_server()

def test_region_picker_present(dash_duo: DashDuo):
    app = get_app()
    dash_duo.start_server(app)

    # Assert region picker component is present
    region_picker = dash_duo.find_element("#region-picker-id")
    assert region_picker.exists()

    dash_duo.stop_server()
