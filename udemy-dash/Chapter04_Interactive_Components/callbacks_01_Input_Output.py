import dash
from dash import dcc  # type: ignore[attr-defined]
from dash import html  # type: ignore[attr-defined]
from dash.dependencies import Input, Output

app = dash.Dash(title=__name__)  # type: ignore[attr-defined]


app.layout = html.Div(
    [
        dcc.Input(
            id="my_input",
            value="my_initial_value",
            type="text",
            style={
                "margin": 5,
                "padding-top": 10,
                "padding-bottom": 10,
                "padding-left": 10,
                "padding-right": 10,
            },
        ),
        html.Div(
            children=[],
            id="my_div",
            style={
                "color": "green",
                "border": "2px blue solid",
                "borderRadius": 10,
                "width": "auto",
                "margin": 5,
                "padding-top": 10,
                "padding-bottom": 10,
                "padding-left": 10,
                "padding-right": 10,
            },
        ),
    ]
)


@app.callback(
    Output(component_id="my_div", component_property="children"),
    Input(component_id="my_input", component_property="value"),
)
def update_output_div(input: dcc.Input) -> str:
    return f"Input: {input}"


if __name__ == "__main__":
    app.run(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_ui=True,
        use_reloader=True,
    )
