from turtle import st
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# import ids  # changed import to run script directly
from . import ids


MEDAL_DATA = px.data.medals_long()  # dummy data


def render(app: Dash) -> html.Div:

    @app.callback(
        Output(ids.BAR_CHART, "children"),
        Input(ids.NATION_DROPDOWN, "value")
    )
    def update_bar_chart(nations: list[str]) -> html.Div:
        # diadvantage: too much python MAGIC -> Id doenst know fnc arg is used
        filtered_nations = MEDAL_DATA.query("nation in @nations")

        # filtered_nations = MEDAL_DATA.loc[MEDAL_DATA.nation.isin(nations)]
        fig = px.bar(filtered_nations, x="medal", y="count",
                     color="nation", text="nation")

        if filtered_nations.shape[0] == 0:
            return html.Div("No data selected")

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    # to create initial bar chart which is changed by callback
    return html.Div(id=ids.BAR_CHART)
