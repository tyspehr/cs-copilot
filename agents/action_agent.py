class ActionAgent:

    def recommend_action(self, row):
        actions = []

        if row["risk_level"] == "High Risk":
            actions.append("Schedule executive business review within 7 days")
            actions.append("Create escalation plan with support leadership")

        if row["risk_level"] == "Moderate Risk":
            actions.append("Launch adoption check-in with account owner")

        if row["feature_adoption_score"] < 50:
            actions.append("Assign product training session")

        if row["login_change_pct"] < -20:
            actions.append("Investigate drop in platform engagement")

        if row["invoice_status"] == "Overdue":
            actions.append("Coordinate with finance on payment status")

        if row["expansion_status"] == "Strong Opportunity":
            actions.append("Prepare expansion business case")

        if row["expansion_status"] == "Moderate Opportunity":
            actions.append("Monitor for expansion timing")

        if not actions:
            actions.append("Continue standard success cadence")

        return " | ".join(actions)

    def analyze(self, master_df):
        df = master_df.copy()

        df["recommended_actions"] = df.apply(
            self.recommend_action,
            axis=1
        )

        return df