import streamlit as st
import plotly.express as px

from agents.data_collector import DataCollectorAgent
from agents.risk_agent import RiskAgent
from agents.expansion_agent import ExpansionAgent
from agents.action_agent import ActionAgent
from agents.executive_brief_agent import ExecutiveBriefAgent
from agents.account_brief_agent import AccountBriefAgent


st.set_page_config(
    page_title="CS Copilot",
    layout="wide"
)

st.title("🤖 Multi-Agent CS Copilot")

st.caption(
    "Connector-ready AI command center for CRM, Support, Usage, and Billing intelligence."
)

data_agent = DataCollectorAgent()
risk_agent = RiskAgent()
expansion_agent = ExpansionAgent()
action_agent = ActionAgent()
brief_agent = ExecutiveBriefAgent()
account_brief_agent = AccountBriefAgent()

master = data_agent.create_master_dataset()
risk_df = risk_agent.analyze(master)
expansion_df = expansion_agent.analyze(risk_df)
final_df = action_agent.analyze(expansion_df)
with st.spinner("Executive Brief Agent analyzing portfolio..."):
    executive_brief = brief_agent.generate_brief(final_df)

st.subheader("Executive Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Accounts", len(final_df))

col2.metric(
    "High Risk Accounts",
    len(final_df[final_df["risk_level"] == "High Risk"])
)

col3.metric(
    "Strong Expansion Opportunities",
    len(final_df[final_df["expansion_status"] == "Strong Opportunity"])
)

col4.metric(
    "Total ARR",
    f"${final_df['arr'].sum():,.0f}"
)

portfolio_health = round(100 - final_df["risk_score"].mean())

with st.sidebar:

    st.title("CS Copilot")

    st.markdown("---")

    st.subheader("Portfolio Overview")

    st.metric(
        "Accounts",
        len(final_df)
    )

    st.metric(
        "Portfolio Health",
        f"{portfolio_health}/100"
    )

    st.metric(
        "High Risk",
        len(
            final_df[
                final_df["risk_level"] == "High Risk"
            ]
        )
    )

    st.metric(
        "Expansion Opps",
        len(
            final_df[
                final_df["expansion_status"] == "Strong Opportunity"
            ]
        )
    )

    st.markdown("---")

    st.subheader("Connector Status")

    st.success("🟢 CRM Connector")
    st.success("🟢 Usage Connector")
    st.success("🟢 Billing Connector")
    st.success("🟢 Support Connector")

    st.markdown("---")

    st.subheader("Current Source")

    source_type = st.selectbox(
        "Data Source",
        [
            "CSV Simulation",
            "Salesforce (Coming Soon)",
            "HubSpot (Coming Soon)",
            "Zendesk (Coming Soon)"
        ]
    )

    st.info(source_type)

    st.markdown("---")

    st.subheader("Available Integrations")

    st.write("• Salesforce")
    st.write("• HubSpot")
    st.write("• Zendesk")
    st.write("• Intercom")
    st.write("• Stripe")
    st.write("• NetSuite")

    st.markdown("---")

    st.caption(
        "Connector-ready multi-agent architecture"
    )

    st.metric(
        "High Risk",
        len(
            final_df[
                final_df["risk_level"] == "High Risk"
            ]
        )
    )

    st.metric(
        "Expansion Opps",
        len(
            final_df[
                final_df["expansion_status"] == "Strong Opportunity"
            ]
        )
    )

    st.markdown("---")

    st.caption(
        "Multi-Agent Customer Success Intelligence Platform"
    )

st.metric(
    "Portfolio Health Score",
    f"{portfolio_health}/100"
)

st.divider()

left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Risk Distribution")

    risk_counts = final_df["risk_level"].value_counts().reset_index()
    risk_counts.columns = ["Risk Level", "Count"]

    fig = px.bar(
        risk_counts,
        x="Risk Level",
        y="Count"
    )

    st.plotly_chart(fig, use_container_width=True)

with right_chart:
    st.subheader("ARR by Risk Level")

    arr_risk = (
        final_df
        .groupby("risk_level")["arr"]
        .sum()
        .reset_index()
    )

    fig2 = px.pie(
        arr_risk,
        values="arr",
        names="risk_level"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("Executive Briefing Agent")

with st.container(border=True):
    st.markdown(executive_brief)

st.divider()

st.subheader("Account-Level AI Copilot")

selected_account = st.selectbox(
    "Select an account",
    final_df["account_name"].tolist()
)

selected_row = final_df[
    final_df["account_name"] == selected_account
].iloc[0]

account_col1, account_col2, account_col3, account_col4 = st.columns(4)

account_col1.metric(
    "ARR",
    f"${selected_row['arr']:,.0f}"
)

account_col2.metric(
    "Risk Score",
    selected_row["risk_score"]
)

account_col3.metric(
    "Expansion Score",
    selected_row["expansion_score"]
)

account_col4.metric(
    "Tickets",
    int(selected_row["total_tickets"])
)

if st.button("Generate Account Brief"):

    with st.spinner("Account Brief Agent analyzing account..."):

        account_brief = (
            account_brief_agent
            .generate_account_brief(selected_row)
        )

    with st.container(border=True):
        st.markdown(account_brief)

st.divider()

st.subheader("Account Command Center")

st.dataframe(
    final_df[
        [
            "account_name",
            "industry",
            "account_owner",
            "arr",
            "renewal_date",
            "risk_score",
            "risk_level",
            "expansion_score",
            "expansion_status",
            "recommended_actions"
        ]
    ],
    use_container_width=True
)

st.divider()

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Highest Risk Accounts")

    high_risk = (
        final_df
        .sort_values("risk_score", ascending=False)
        .head(5)
    )

    st.dataframe(
        high_risk[
            [
                "account_name",
                "arr",
                "risk_score",
                "risk_level",
                "recommended_actions"
            ]
        ],
        use_container_width=True
    )

with right_col:
    st.subheader("Top Expansion Opportunities")

    expansion = (
        final_df
        .sort_values("expansion_score", ascending=False)
        .head(5)
    )

    st.dataframe(
        expansion[
            [
                "account_name",
                "arr",
                "potential_expansion_value",
                "expansion_score",
                "expansion_status"
            ]
        ],
        use_container_width=True
    )

st.divider()

st.subheader("Recommended Actions")

st.dataframe(
    final_df[
        [
            "account_name",
            "risk_level",
            "expansion_status",
            "recommended_actions"
        ]
    ],
    use_container_width=True
)

st.divider()

st.subheader("Agent Activity Feed")

for _, row in final_df.iterrows():
    if row["risk_level"] == "High Risk":
        st.warning(
            f"[Risk Agent] Flagged {row['account_name']} "
            f"(Risk Score: {row['risk_score']})"
        )

    if row["expansion_status"] == "Strong Opportunity":
        st.success(
            f"[Expansion Agent] Identified growth opportunity in "
            f"{row['account_name']} "
            f"(Expansion Score: {row['expansion_score']})"
        )

st.info("[Executive Brief Agent] Portfolio summary generated successfully.")