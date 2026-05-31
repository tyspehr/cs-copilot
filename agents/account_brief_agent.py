import os
import streamlit as st

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = (
    st.secrets.get("OPENAI_API_KEY")
    or os.getenv("OPENAI_API_KEY")
)

client = OpenAI(
    api_key=api_key
)


class AccountBriefAgent:

    def generate_account_brief(self, row):

        prompt = f"""
You are a Customer Success leader preparing for an account review.

Create a concise account brief using the following data:

Account Name: {row["account_name"]}
Industry: {row["industry"]}
ARR: ${row["arr"]:,.0f}
Renewal Date: {row["renewal_date"]}
CRM Health Score: {row["crm_health_score"]}
Feature Adoption Score: {row["feature_adoption_score"]}
Login Change Percent: {row["login_change_pct"]}
Invoice Status: {row["invoice_status"]}
Days Overdue: {row["days_overdue"]}
Total Support Tickets: {row["total_tickets"]}
Risk Score: {row["risk_score"]}
Risk Level: {row["risk_level"]}
Expansion Score: {row["expansion_score"]}
Expansion Status: {row["expansion_status"]}
Recommended Actions: {row["recommended_actions"]}

Write the brief with these sections:
1. Account Snapshot
2. Risk Drivers
3. Expansion Potential
4. Recommended Next Steps

Keep it executive-ready and practical.
"""

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert Customer Success strategist."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content