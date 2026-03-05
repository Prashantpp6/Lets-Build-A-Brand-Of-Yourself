# analyzer.py

def analyze_behavior(productivity, learning, networking, content, health):
    """
    Analyze user habits and detect weak areas.
    """

    insights = []

    if productivity < 5:
        insights.append("Your productivity is low. Improve focus and time management.")

    if learning < 5:
        insights.append("Learning hours are low. Invest more time in skill development.")

    if networking < 5:
        insights.append("Your networking activity is weak. Build connections on LinkedIn.")

    if content < 5:
        insights.append("Content creation is inconsistent. Sharing knowledge builds authority.")

    if health < 5:
        insights.append("Health habits need improvement. Exercise and rest are important.")

    if len(insights) == 0:
        insights.append("Great job! Your habits support strong personal brand growth.")

    return insights