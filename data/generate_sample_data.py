import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

companies = [
    "Northstar Health",
    "BrightPath Logistics",
    "Summit Retail Group",
    "BlueRiver Manufacturing",
    "Pinnacle Finance",
    "MetroCare Clinics",
    "Apex Hospitality",
    "Crescent Foods",
    "Ironwood Construction",
    "Valley Medical Partners"
]

industries = [
    "Healthcare",
    "Logistics",
    "Retail",
    "Manufacturing",
    "Finance",
    "Healthcare",
    "Hospitality",
    "Food & Beverage",
    "Construction",
    "Healthcare"
]

owners = [
    "Tyler Spehr",
    "Jamie Lee",
    "Morgan Patel",
    "Alex Rivera"
]

crm_rows = []
usage_rows = []
billing_rows = []
support_rows = []

for i, company in enumerate(companies, start=1):

    account_id = f"ACC-{1000+i}"

    arr = random.randint(50000, 500000)

    renewal_date = (
        datetime.today()
        + timedelta(days=random.randint(20, 240))
    )

    crm_rows.append({
        "account_id": account_id,
        "account_name": company,
        "industry": industries[i-1],
        "arr": arr,
        "account_owner": random.choice(owners),
        "renewal_date": renewal_date.date(),
        "crm_health_score": random.randint(30, 95)
    })

    usage_rows.append({
        "account_id": account_id,
        "monthly_active_users": random.randint(10, 500),
        "licensed_users": random.randint(50, 600),
        "feature_adoption_score": random.randint(20, 100),
        "login_change_pct": random.randint(-50, 50)
    })

    billing_rows.append({
        "account_id": account_id,
        "invoice_status": random.choice(
            ["Current", "Current", "Current", "Overdue"]
        ),
        "days_overdue": random.choice(
            [0, 0, 0, 15, 30, 60]
        ),
        "contract_value": arr,
        "potential_expansion_value": random.randint(
            10000,
            150000
        )
    })

    for t in range(random.randint(2, 8)):

        support_rows.append({
            "ticket_id": f"TKT-{i}{t}",
            "account_id": account_id,
            "severity": random.choice(
                ["Low", "Medium", "High", "Critical"]
            ),
            "status": random.choice(
                ["Open", "Closed", "Pending"]
            ),
            "sentiment": random.choice(
                ["Positive", "Neutral", "Negative"]
            )
        })

pd.DataFrame(crm_rows).to_csv(
    "data/crm_accounts.csv",
    index=False
)

pd.DataFrame(usage_rows).to_csv(
    "data/product_usage.csv",
    index=False
)

pd.DataFrame(billing_rows).to_csv(
    "data/billing_data.csv",
    index=False
)

pd.DataFrame(support_rows).to_csv(
    "data/support_tickets.csv",
    index=False
)

print("Enterprise datasets generated.")