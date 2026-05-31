import pandas as pd


class UsageConnector:

    def __init__(self, source="csv"):
        self.source = source

    def fetch_usage(self):
        if self.source == "csv":
            return pd.read_csv("data/product_usage.csv")

        raise NotImplementedError(
            "Product usage API connector not implemented yet."
        )