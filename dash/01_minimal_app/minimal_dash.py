from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1('Gapminder Data'),
    dcc.Dropdown(df.country.unique(), 'Austria', id='dropdown-select'),
    dcc.Graph(id='graph-output')
])


@app.callback(
    Output('graph-output', 'figure'),
    Input('dropdown-select', 'value')
)
def update_graph(country):
    dff = df[df.country == country]
    fig = px.line(dff, x='year', y='pop', title=f'Population in {country}')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
