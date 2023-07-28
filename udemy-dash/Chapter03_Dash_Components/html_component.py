import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()


# using list of divs
# using style={"property": "value"}
app.layout = html.Div(
    [
        "Outer Div",
        html.Div(
            ["First Inner Div"],
            style={
                "width": 250,
                "height": 100,
                "color": "green",
                "border": "2px red dashed",
                "borderRadius": 5,
            },
        ),
        html.Div(
            "Second Inner Div",
            style={
                "color": "green",
                "border": "2px blue solid",
                "borderRadius": 20,
                "width": 200,
                "margin": 10,
            },
        ),
    ],
    style={"width": 500, "height": 200, "color": "red", "border": "2px green dotted"},
)


if __name__ == "__main__":
    app.run_server()
