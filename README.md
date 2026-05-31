# CS Copilot

CS Copilot is a multi-agent Customer Success intelligence platform that analyzes CRM, support, billing, and product usage data to identify customer risk, uncover expansion opportunities, recommend actions, and generate AI-powered executive briefings.

The project is built as a connector-ready platform: it currently runs on simulated CSV data, but the architecture is designed so real systems like Salesforce, HubSpot, Zendesk, Stripe, and NetSuite can be plugged in later.

---

## What It Does

CS Copilot helps Customer Success and Revenue teams answer questions like:

* Which accounts are most at risk?
* Which customers have expansion potential?
* What actions should the CSM or leadership team take next?
* What should executives know about the portfolio this week?
* What does a specific account need before renewal?

---

## Key Features

* Multi-agent architecture
* Connector abstraction layer
* Portfolio health scoring
* Risk analysis by account
* Expansion opportunity scoring
* Recommended action generation
* AI-generated executive briefings
* AI-generated account-level briefs
* Streamlit dashboard
* Simulated enterprise CRM, support, usage, and billing datasets

---

## Agent Architecture

The system uses specialized agents that each perform a specific business function:

1. **Data Collector Agent**
   Loads CRM, usage, billing, and support data through connector classes.

2. **Risk Agent**
   Scores accounts based on customer health, adoption, usage trends, support activity, and billing status.

3. **Expansion Agent**
   Identifies accounts with strong growth potential based on adoption, health, and expansion value.

4. **Action Agent**
   Recommends next steps for each account.

5. **Executive Brief Agent**
   Uses OpenAI to generate a portfolio-level executive summary.

6. **Account Brief Agent**
   Uses OpenAI to generate account-specific Customer Success briefs.

---

## Architecture Diagram

```text
CRM Data
Usage Data
Billing Data
Support Data
      │
      ▼
Connectors
      │
      ▼
Data Collector Agent
      │
      ▼
Risk Agent
      │
      ▼
Expansion Agent
      │
      ▼
Action Agent
      │
      ▼
Executive Brief Agent
      │
      ▼
Account Brief Agent
      │
      ▼
Streamlit Dashboard
```

---

## Connector-Ready Design

Current data source:

* CSV simulation data

Connector classes are already separated into:

* CRM Connector
* Usage Connector
* Billing Connector
* Support Connector

Future integrations could include:

* Salesforce
* HubSpot
* Zendesk
* Intercom
* Stripe
* NetSuite

This allows the rest of the agent pipeline to remain unchanged while swapping CSV simulation data for real API-based data sources.

---

## Technology Stack

* Python
* Streamlit
* Pandas
* Plotly
* OpenAI API
* python-dotenv
* GitHub

---

## Project Structure

```text
cs-copilot/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── agents/
│   ├── data_collector.py
│   ├── risk_agent.py
│   ├── expansion_agent.py
│   ├── action_agent.py
│   ├── executive_brief_agent.py
│   └── account_brief_agent.py
│
├── connectors/
│   ├── crm_connector.py
│   ├── usage_connector.py
│   ├── billing_connector.py
│   └── support_connector.py
│
├── data/
│   ├── generate_sample_data.py
│   ├── crm_accounts.csv
│   ├── product_usage.csv
│   ├── billing_data.csv
│   └── support_tickets.csv
│
└── screenshots/
```

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/tyspehr/cs-copilot.git
cd cs-copilot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```bash
touch .env
```

Add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

### 4. Generate sample data

```bash
python data/generate_sample_data.py
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## Example Use Cases

* Customer Success portfolio reviews
* Executive account briefings
* Renewal risk analysis
* Expansion opportunity planning
* RevOps dashboarding
* AI-assisted account management workflows

---

## Future Roadmap

* Salesforce API integration
* HubSpot API integration
* Zendesk ticket integration
* Stripe or NetSuite billing connector
* PDF executive report export
* Slack delivery
* Email delivery
* Scheduled weekly portfolio reviews
* Account playbook generation
* Churn prediction modeling

---
## Screenshots

### Executive Metrics Dashboard

![Executive Metrics](Co-Pilot%20Screenshots/Demo%20-%20Executive%20Metrics%201.png)

---

### Risk Distribution Analysis

![Risk Distribution](Co-Pilot%20Screenshots/Demo%20-%20Risk%20Distribution.png)

---

### Executive Briefing Agent

![Executive Briefing Agent](Co-Pilot%20Screenshots/Demo%20-%20Executive%20Briefing%20Agent.png)

---

### Account-Level AI Copilot

![Account AI Copilot](Co-Pilot%20Screenshots/Demo%20-%20Account%20level%20AI%20Copilot.png)

---

### AI Generated Account Brief

![Generated AI Account Brief](Co-Pilot%20Screenshots/Demo%20-%20Generated%20AI%20Account%20Brief.png)

---

### Agent Activity Feed

![Agent Activity Feed](Co-Pilot%20Screenshots/Demo%20-%20Agent%20Activity%20Feed.png)

---

### Connector Architecture Sidebar

![Connector Status Sidebar](Co-Pilot%20Screenshots/Demo%20-%20Connector%20Status%20Sidebar.png)

---

### Navigation Sidebar

![Sidebar 1](Co-Pilot%20Screenshots/Demo%20-%20Sidebar%201.png)

![Sidebar 2](Co-Pilot%20Screenshots/Demo%20-%20Sidebar%202.png)
---

## Why I Built This

I built CS Copilot to explore how AI agents can support Customer Success and Revenue teams by reducing manual reporting work and turning scattered customer data into actionable insights.

Rather than building a generic chatbot, this project focuses on a real business workflow: aggregating customer data, identifying risk, surfacing expansion opportunities, recommending actions, and generating executive-ready summaries.

Disclaimer: This project uses simulated data and was created as a personal learning project to explore AI-assisted Customer Success workflows. It is not affiliated with or endorsed by any employer, customer, or third-party organization.


---

## Author

**Tyler Spehr**
Customer Success | Revenue Operations | AI Automation
