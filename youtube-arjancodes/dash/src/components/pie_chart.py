import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
# from youtube-arjancodes.dash.src.data.loader import DataSchema
from ..data.loader import DataSchema

# import ids  # changed import to run script directly
from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:

    @app.callback(
        Output(ids.PIE_CHART, "children"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.MONTH_DROPDOWN, "value"),
         Input(ids.CATEGORY_DROPDOWN, "value")],
    )
    def update_pie_chart(years: list[str], months: list[str], categories: list[str]) -> html.Div:
        filtered_data = data.query(
            "year in @years and month in  @months and category in @categories")

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected")

        pie = go.Pie(
            labels=filtered_data[DataSchema.CATEGORY].tolist(),
            values=filtered_data[DataSchema.AMOUNT].tolist(),
            hole=0.5,
        )

        fig = go.Figure(data=[pie])

        return html.Div(dcc.Graph(figure=fig), id=ids.PIE_CHART)

    # to create initial bar chart-Div which is changed by callback
    return html.Div(id=ids.PIE_CHART)
