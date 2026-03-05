def calculate_brand_score(productivity, learning, networking, content, health):

    productivity_weight = 0.25
    learning_weight = 0.25
    networking_weight = 0.20
    content_weight = 0.15
    health_weight = 0.15

    brand_score = (
        productivity * productivity_weight +
        learning * learning_weight +
        networking * networking_weight +
        content * content_weight +
        health * health_weight
    )

    return round(brand_score, 2)


def regret_risk(score):

    if score >= 8:
        return "Low Regret Risk"

    elif score >= 5:
        return "Medium Regret Risk"

    else:
        return "High Regret Risk"