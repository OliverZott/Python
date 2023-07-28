import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# First Sample

# generate data
np.random.seed(42)
x_vals = np.linspace(0, 1, 100)
y_vals = np.random.randn(100)

trace1 = go.Scatter(
    x=x_vals,
    y=y_vals,
    mode='lines',
    name='lines')

trace2 = go.Scatter(
    x=x_vals,
    y=y_vals+5,
    mode='markers+lines',
    name='markers+lines')

trace3 = go.Scatter(
    x=x_vals,
    y=y_vals-5,
    mode='markers',
    name='markers')

data = [trace1, trace2, trace3]


layout = go.Layout(title='Line Charts')


fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)


# Real data sample

# import data
df = pd.read_csv('../data/nst-est2017-alldata.csv')

df.head()
