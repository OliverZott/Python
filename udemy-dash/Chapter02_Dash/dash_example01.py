import dash
import dash_core_components as dcc
import dash_html_components as html

# start flasl server in background
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children="Hello Dash"),
    html.Div(children="Dash: WebApp"),

    dcc.Graph(
        id="graph1",
        figure={
            "data": [
                {"x": [1, 2, 3],
                 "y": [4, 1, 6],
                 "type": "bar",
                 "name": "sample plot 1"},
                {"x": [1, 2, 3],
                 "y": [2, 4, 3],
                 "type": "bar",
                 "name": "sample plot 2"}
            ],
            "layout": {"title": "Dash Visualization"}
        }
    )
])


if __name__ == "__main__":
    app.run_server()
