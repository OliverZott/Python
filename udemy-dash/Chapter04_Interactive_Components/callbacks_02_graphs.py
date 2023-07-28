import dash
import pandas as pd
import plotly.graph_objs as go
from dash import dcc  # type: ignore[attr-defined]
from dash import html
from dash.dependencies import Input, Output

df = pd.read_csv("udemy-dash/data/gapminderDataFiveYear.csv")
print(df.head())


year_options = []
for year in df["year"].unique():
    year_options.append({"label": str(year), "value": year})

app = dash.Dash(title=__name__)

app.layout = html.Div(
    [
        dcc.Graph(
            id="graph-gapminder",
        ),
        dcc.Dropdown(
            id="year-dropdown",
            options=year_options,
            # value=df["year"].min(),
        ),
    ]
)


@app.callback(
    Output(component_id="graph-gapminder", component_property="figure"),
    Input(component_id="year-dropdown", component_property="value"),
)
def update_graph(selected_year: str) -> dict:
    df_by_year = df[df["year"] == selected_year]

    traces = []

    for continent_name in df_by_year["continent"].unique():
        df_by_continent = df_by_year[df_by_year["continent"] == continent_name]

        traces.append(
            go.Scatter(
                x=df_by_continent["gdpPercap"],
                y=df_by_continent["lifeExp"],
                text=df_by_continent["country"],
                name=continent_name,
                mode="markers",
                marker=dict(size=12),
                opacity=0.8,
            )
        )

    return {
        "data": traces,
        "layout": go.Layout(
            title="My scatter plot 2",
            xaxis={
                "title": "GDP Per Cap",
                "type": "log",
            },
            yaxis={"title": "Life Expectancy"},
        ),
    }


if __name__ == "__main__":
    app.run(
        debug=True,
        dev_tools_hot_reload=True,
        dev_tools_ui=True,
        use_reloader=True,
    )
