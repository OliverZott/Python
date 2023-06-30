import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

# Data
#   D ...date im August
#   X ...duration of eruption (min)
#   Y ...interval to next eruption
df = pd.read_csv("udemy-dash/data/OldFaithful.csv")
# print(df)
# print(df["X"])


app.layout = html.Div([
    dcc.Graph(
        id="oldfaithful",
        figure={
            "data": [go.Scatter(
                x=df["X"],
                y=df["Y"],
                mode="markers",
                marker={
                    "size": 10,
                    "color": 'LightSkyBlue',
                    "symbol": "circle",
                    "line": {"width": 1.5},
                    "opacity": 0.5,
                }
            )],
            "layout": go.Layout(
                title="Old Faithful: Eruption duration vs. Intervals",
                xaxis={"title": "Duration of eruption (minutes)"},
                yaxis={"title": "Intervals to next eruption (minutes)"}
            )
        }
    )
])


if __name__ == "__main__":
    app.run()
