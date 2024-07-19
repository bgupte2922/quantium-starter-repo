from app import dash_app


def test_header_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#header", timeout=20)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#visualization", timeout=20)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#region_picker", timeout=20)

"""
To run above code:
1. Open a terminal or command prompt.
2. Navigate to the directory where test_pink_morsel_visualizer.py is saved using the cd command.
3. Run the script: pytest test_pink_morsel_visualizer.py
"""