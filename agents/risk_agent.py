class RiskAgent:

    def calculate_risk_score(self, row):
        score = 0

        if row["crm_health_score"] < 50:
            score += 25

        if row["feature_adoption_score"] < 50:
            score += 20

        if row["login_change_pct"] < -20:
            score += 20

        if row["total_tickets"] >= 5:
            score += 15

        if row["invoice_status"] == "Overdue":
            score += 10

        if row["days_overdue"] >= 30:
            score += 10

        return min(score, 100)

    def classify_risk(self, score):
        if score >= 70:
            return "High Risk"
        elif score >= 40:
            return "Moderate Risk"
        else:
            return "Low Risk"

    def analyze(self, master_df):
        df = master_df.copy()

        df["risk_score"] = df.apply(
            self.calculate_risk_score,
            axis=1
        )

        df["risk_level"] = df["risk_score"].apply(
            self.classify_risk
        )

        return df