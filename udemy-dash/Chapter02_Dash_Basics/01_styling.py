import dash_core_components as dcc
import dash_html_components as html

import dash

# start flasl server in background
app = dash.Dash()

colors = {"background1": "#111111", "background2": "#441137", "text": "#7FDBFF"}

app.layout = html.Div(
    children=[
        html.H1("Hello Dash", style={"textAlign": "center", "color": colors["text"]}),
        html.Div(children="Dash: WebApp"),
        dcc.Graph(
            id="graph1",
            figure={
                "data": [
                    {
                        "x": [1, 2, 3],
                        "y": [4, 1, 6],
                        "type": "bar",
                        "name": "sample plot 1",
                    },
                    {
                        "x": [1, 2, 3],
                        "y": [2, 4, 3],
                        "type": "bar",
                        "name": "sample plot 2",
                    },
                ],
                "layout": {
                    "plot_bgcolor": colors["background1"],
                    "paper_bgcolor": colors["background1"],
                    "font": {"color": colors["text"]},
                    "title": "Dash Visualization",
                },
            },
        ),
    ],
    style={"backgroundColor": colors["background2"]},
)


if __name__ == "__main__":
    app.run_server()
