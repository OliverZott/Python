import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input
from dash.dependencies import Output

import dash
from dash import dcc
from dash import html

# Data
df = pd.read_csv("udemy-dash/data/mpg.csv")
print(df.head())


# Input arguments
features = df.columns


# Dash App
app = dash.Dash(title=__name__)

app.layout = html.Div(
    id="outer-div",
    children=[
        html.Div(
            id="dropdown-div1",
            children=dcc.Dropdown(
                id="xdropdown",
                options=features,
                value="horsepower",
            ),
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            id="dropdown-div2",
            children=dcc.Dropdown(
                id="ydropdown",
                options=[{"label": i, "value": i} for i in features],
                value="mpg",
            ),
            style={"width": "48%", "display": "inline-block", "float": "right"},
        ),
        dcc.Graph(
            id="graph",
        ),
    ],
    style=dict(padding=55),
)


# Dash Callbacks
@app.callback(
    Output(component_id="graph", component_property="figure"),
    Input(component_id="xdropdown", component_property="value"),
    Input(component_id="ydropdown", component_property="value"),
)
def update_x_dropdown(xdropdown: str, ydropdown: str) -> dict:
    data = [
        go.Scatter(
            x=df[xdropdown],
            y=df[ydropdown],
            text=df["name"],
            mode="markers",
            marker=dict(
                size=15,
                opacity=0.6,
                line={"width": 1.5, "color": "black"},
            ),
        )
    ]
    return {
        "data": data,
        "layout": go.Layout(
            title="mpg-plot",
            xaxis=dict(title=xdropdown.title()),
            yaxis=dict(title=ydropdown),
        ),
    }


# Run App
if __name__ == "__main__":
    app.run(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_ui=True,
        use_reloader=True,
    )
