import os

import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dotenv import load_dotenv

import dash
from dash import dcc, html

load_dotenv()

DATA_BASE_PATH = str(os.getenv("DATA_BASE_PATH"))
file_name = "mpg.csv"
file_path = os.path.join(DATA_BASE_PATH, file_name)

# Data
df = pd.read_csv(file_path)
# print(df.head())


# Dash App
app = dash.Dash(title=__name__)

app.layout = html.Div()


# Run App
if __name__ == "__main__":
    app.run(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_ui=True,
        use_reloader=True,
    )
