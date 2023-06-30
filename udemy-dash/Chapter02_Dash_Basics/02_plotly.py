import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go

app = dash.Dash()

# Daten
np.random.seed(42)
ran_x = np.random.randint(1, 101, 100)
ran_y = np.random.randint(1, 101, 100)


# Layout
app.layout = html.Div([
    dcc.Graph(
        id="scatter",
        figure={
            "data": [go.Scatter(
                x=ran_x,
                y=ran_y,
                mode="markers",
                marker={
                    "size": 15,
                    "color": "rgb(52,156,152)",
                    "symbol": "square",
                    "line": {"width": 2}
                }
            )],
            "layout": go.Layout(
                title="My scatter plot",
                xaxis={"title": "X - Axis"})
        },
    ),
    dcc.Graph(
        id="scatter2",
        figure={
            "data": [go.Scatter(
                x=ran_x,
                y=ran_y,
                mode="markers",
                marker={
                    "size": 15,
                    "color": 'LightSkyBlue',
                    "symbol": "circle",
                    "line": {"width": 2},
                    "opacity": 0.5,
                }
            )],
            "layout": go.Layout(
                title="My scatter plot 2",
                xaxis={"title": "X - Axis"})
        },
    )
])


if __name__ == "__main__":
    app.run()
