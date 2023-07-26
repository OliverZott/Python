import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input
from dash.dependencies import Output

import dash
from dash import dcc  # type: ignore[attr-defined]
from dash import html

df = pd.read_csv("../data/gapminderDataFiveYear.csv")

app = dash.Dash(title=__name__)


if __name__ == "__main__":
    app.run(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_ui=True,
        use_reloader=True,
    )
