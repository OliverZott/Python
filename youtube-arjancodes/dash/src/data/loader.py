from unicodedata import category
from xmlrpc.client import DateTime
import pandas as pd


class DataSchema:
    AMOUNT = "amount"
    CATEGORY = "category"
    DATE = "date"
    YEAR = "year"
    MONTH = "month"

# class Transaction:
#     amount: str
#     category: str
#     date: DateTime


def load_transaction_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(
        path,
        dtype={
            DataSchema.AMOUNT: float,
            DataSchema.CATEGORY: str
        },
        parse_dates=[DataSchema.DATE]
    )

    data[DataSchema.YEAR] = data[DataSchema.DATE].dt.year.astype(str)
    data[DataSchema.MONTH] = data[DataSchema.DATE].dt.month.astype(str)

    return data
