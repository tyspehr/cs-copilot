import pandas as pd


class BillingConnector:

    def __init__(self, source="csv"):
        self.source = source

    def fetch_billing(self):
        if self.source == "csv":
            return pd.read_csv("data/billing_data.csv")

        raise NotImplementedError(
            "Stripe/NetSuite billing connector not implemented yet."
        )