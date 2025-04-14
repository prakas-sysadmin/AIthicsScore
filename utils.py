def calculate_final_score(bias_score, privacy_score, governance_score):
    total = (bias_score * 0.4) + (privacy_score * 0.3) + (governance_score * 0.3)
    return round(total, 2)
