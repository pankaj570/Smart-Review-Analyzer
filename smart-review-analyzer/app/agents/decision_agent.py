def make_decision(churn_risk, insights):
    if churn_risk == 1:
        return "Escalate to Manager"
    return "Send Appreciative Email"
