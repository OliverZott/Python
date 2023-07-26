import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

# generate random data
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data = [
    go.Scatter(
        x=random_x,
        y=random_y,
        mode="markers",
        marker=dict(
            size=20,
            color="rgb(50,200,150)",
            symbol="square",
            line={"width": 4},
        ),
    )
]


# Generate layout
layout = go.Layout(
    title="First ScatterPlot",
    xaxis=dict(
        title="MY X AXIS",
    ),
    yaxis={"title": "MY Y AXIS"},
    hovermode="closest",
)


fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
