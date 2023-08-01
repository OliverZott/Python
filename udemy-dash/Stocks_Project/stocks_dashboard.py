import dash
from dash import html

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
