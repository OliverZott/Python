from dash import Dash, html
from . import pie_chart
from . import bar_chart
from . import category_dropdown
from . import month_dropdown
from . import year_dropdown
import pandas as pd


def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(app, data),
                    month_dropdown.render(app, data),
                    category_dropdown.render(app, data),
                ],
                style={"width": "40%"},
            ),
            bar_chart.render(app, data),
            pie_chart.render(app, data)
        ],
    )
