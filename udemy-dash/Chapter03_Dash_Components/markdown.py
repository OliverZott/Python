import dash
from dash import dcc, html

app = dash.Dash()

markdown_text = """
# My Markdown Example

## part1
Dash documentation:
[link](https://dash.plotly.com/) 

## part2

- test
- test
"""

app.layout = html.Div([dcc.Markdown(children=markdown_text)])

if __name__ == "__main__":
    app.run()
