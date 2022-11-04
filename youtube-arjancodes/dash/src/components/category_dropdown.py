import pandas as pd
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from ..data.loader import DataSchema

from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:

    all_categories: list[str] = data[DataSchema.CATEGORY].tolist()
    unique_categories = sorted(set(all_categories))

    @app.callback(
        Output(component_id=ids.CATEGORY_DROPDOWN,
               component_property="value"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.MONTH_DROPDOWN, "value"),
         Input(ids.SELECT_ALL_CATEGORIES_BUTTON, "n_clicks")],
    )
    def select_all_categories(years: list[str], months: list[str], _: int) -> list[str]:
        filtered_data = data.query("year in @years and month in @months")
        return sorted(set(filtered_data[DataSchema.CATEGORY].tolist()))

    return html.Div(
        children=[
            html.H6("Category"),
            dcc.Dropdown(
                id=ids.CATEGORY_DROPDOWN,
                options=[{"label": category, "value": category}
                         for category in unique_categories],
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_CATEGORIES_BUTTON
            )
        ],
    )
