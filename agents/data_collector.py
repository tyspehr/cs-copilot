from connectors.crm_connector import CRMConnector
from connectors.usage_connector import UsageConnector
from connectors.billing_connector import BillingConnector
from connectors.support_connector import SupportConnector


class DataCollectorAgent:

    def __init__(self, source="csv"):
        self.crm_connector = CRMConnector(source)
        self.usage_connector = UsageConnector(source)
        self.billing_connector = BillingConnector(source)
        self.support_connector = SupportConnector(source)

    def load_data(self):
        crm = self.crm_connector.fetch_accounts()
        usage = self.usage_connector.fetch_usage()
        billing = self.billing_connector.fetch_billing()
        tickets = self.support_connector.fetch_tickets()

        return crm, usage, billing, tickets

    def create_master_dataset(self):
        crm, usage, billing, tickets = self.load_data()

        ticket_summary = (
            tickets.groupby("account_id")
            .agg(
                total_tickets=("ticket_id", "count")
            )
            .reset_index()
        )

        master = (
            crm
            .merge(usage, on="account_id", how="left")
            .merge(billing, on="account_id", how="left")
            .merge(ticket_summary, on="account_id", how="left")
        )

        master["total_tickets"] = (
            master["total_tickets"]
            .fillna(0)
        )

        return master