import os
from dash import Dash, html
from src.components.layout import create_layout
from src.data.loader import load_transaction_data
from dash_bootstrap_components.themes import BOOTSTRAP

DATA_PATH = "./data/transactions.csv"
# pathh = os.path.abspath(DATA_PATH)
pathh = os.path.join(os.getcwd(), DATA_PATH)


def main() -> None:
    data = load_transaction_data(pathh)
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Financial Dashboard"
    app.layout = create_layout(app, data)
    app.run()


if __name__ == "__main__":
    main()
