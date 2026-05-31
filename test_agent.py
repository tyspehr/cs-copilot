from agents.data_collector import DataCollectorAgent
from agents.risk_agent import RiskAgent
from agents.expansion_agent import ExpansionAgent

data_agent = DataCollectorAgent()
risk_agent = RiskAgent()
expansion_agent = ExpansionAgent()

master = data_agent.create_master_dataset()

risk_df = risk_agent.analyze(master)

final_df = expansion_agent.analyze(risk_df)

print(
    final_df[
        [
            "account_name",
            "risk_level",
            "risk_score",
            "expansion_score",
            "expansion_status"
        ]
    ]
)