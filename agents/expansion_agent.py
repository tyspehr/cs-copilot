class ExpansionAgent:

    def identify_expansion(self, row):

        score = 0

        if row["crm_health_score"] >= 70:
            score += 25

        if row["feature_adoption_score"] >= 70:
            score += 25

        if row["invoice_status"] == "Current":
            score += 20

        if row["login_change_pct"] > 0:
            score += 15

        if row["potential_expansion_value"] > 50000:
            score += 15

        return score

    def classify(self, score):

        if score >= 75:
            return "Strong Opportunity"

        if score >= 50:
            return "Moderate Opportunity"

        return "Limited Opportunity"

    def analyze(self, master_df):

        df = master_df.copy()

        df["expansion_score"] = df.apply(
            self.identify_expansion,
            axis=1
        )

        df["expansion_status"] = (
            df["expansion_score"]
            .apply(self.classify)
        )

        return df