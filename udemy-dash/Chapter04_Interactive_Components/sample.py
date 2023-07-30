import dash_html_components as html
from dash.dependencies import Input
from dash.dependencies import Output

import dash

app = dash.Dash(__name__)

app.layout = html.Div([html.Button("Click me", id="button"), html.Div(id="output")])


@app.callback(Output("output", "children"), [Input("button", "n_clicks")])
def update_output(n_clicks):
    print("update_output called")
    return f"Button clicked {n_clicks} times"


if __name__ == "__main__":
    app.run_server(debug=True)
