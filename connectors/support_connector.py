import pandas as pd


class SupportConnector:

    def __init__(self, source="csv"):
        self.source = source

    def fetch_tickets(self):
        if self.source == "csv":
            return pd.read_csv("data/support_tickets.csv")

        raise NotImplementedError(
            "Zendesk/Intercom support connector not implemented yet."
        )