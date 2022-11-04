import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
# from youtube-arjancodes.dash.src.data.loader import DataSchema
from ..data.loader import DataSchema

# import ids  # changed import to run script directly
from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:

    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [Input(ids.YEAR_DROPDOWN, "value"),
         Input(ids.MONTH_DROPDOWN, "value"),
         Input(ids.CATEGORY_DROPDOWN, "value")],
    )
    def update_bar_chart(years: list[str], months: list[str], categories: list[str]) -> html.Div:
        # disadvantage: too much python MAGIC -> Id doesnt know function arg is used
        filtered_data = data.query(
            "year in @years and month in  @months and category in @categories")
        # filtered_data = data.loc[data.year.isin(years)]

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected")

        pivot_table = create_pivot_table(filtered_data)

        fig = px.bar(
            pivot_table,
            x=DataSchema.CATEGORY,
            y=DataSchema.AMOUNT,
            color=DataSchema.CATEGORY,
            text="category"
        )

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    # to create initial bar chart-Div which is changed by callback
    return html.Div(id=ids.BAR_CHART)


def create_pivot_table(filterd_data: pd.DataFrame) -> pd.DataFrame:
    pt = filterd_data.pivot_table(
        values=DataSchema.AMOUNT,
        index=[DataSchema.CATEGORY],
        aggfunc="sum",
        fill_value=0
    )
    return pt.reset_index().sort_values(DataSchema.AMOUNT, ascending=False)
