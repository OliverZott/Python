from ast import In
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from . import ids


def render(app: Dash) -> html.Div:
    all_nations = ["South Korea", "China", "Canada"]

    @app.callback(
        Output(component_id=ids.NATION_DROPDOWN, component_property="value"),
        Input(ids.SELECT_ALL_NATIONS, "n_clicks")
    )
    def select_all_nations(_: int) -> list[str]:
        return all_nations

    return html.Div(
        children=[
            html.H6("Nation"),
            dcc.Dropdown(
                id=ids.NATION_DROPDOWN,
                options=[{"label": nation, "value": nation}
                         for nation in all_nations],  # list comprehension
                value=all_nations,
                multi=True
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_NATIONS
            )
        ]
    )
