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


class ExecutiveBriefAgent:

    def generate_brief(self, df):

        portfolio_data = df[
            [
                "account_name",
                "arr",
                "risk_score",
                "risk_level",
                "expansion_score",
                "expansion_status",
                "recommended_actions"
            ]
        ].to_dict(orient="records")

        prompt = f"""
You are a VP of Customer Success.

Review the following portfolio data and generate an executive briefing.

Focus on:

- Overall portfolio health
- High-risk accounts
- Revenue exposure
- Expansion opportunities
- Recommended leadership actions

Portfolio Data:

{portfolio_data}

Write the briefing as if it were being sent to a CRO, CEO, or VP of Customer Success.
"""

        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an experienced Customer Success executive."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content