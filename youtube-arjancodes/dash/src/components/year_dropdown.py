import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from ..data.loader import DataSchema  # Import file from different path !!!

from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_years: list[str] = data[DataSchema.YEAR].tolist()
    unique_years = sorted(set(all_years), key=int)

    @app.callback(
        Output(component_id=ids.YEAR_DROPDOWN,
               component_property="value"),
        Input(component_id=ids.SELECT_ALL_YEARS_BUTTON,
              component_property="n_clicks"),
    )
    def select_all_years(_: int) -> list[str]:
        return unique_years

    return html.Div(
        children=[
            html.H6("Year"),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=[{"label": year, "value": year}
                         for year in unique_years],  # list comprehension
                value="blub",  # unique_years
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_YEARS_BUTTON
            )
        ],
    )
