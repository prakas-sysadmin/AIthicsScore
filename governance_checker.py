def check_governance(answers: dict):
    score = 0
    for key, val in answers.items():
        if val.lower() == "yes":
            score += 20
    return score
