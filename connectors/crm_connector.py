import pandas as pd


class CRMConnector:

    def __init__(self, source="csv"):
        self.source = source

    def fetch_accounts(self):
        if self.source == "csv":
            return pd.read_csv("data/crm_accounts.csv")

        raise NotImplementedError(
            "Salesforce/HubSpot connector not implemented yet."
        )