# recommendation.py

def generate_recommendations(productivity, learning, networking, content, health):
    """
    Generate actionable recommendations to improve personal brand.
    """

    recommendations = []

    if productivity < 5:
        recommendations.append(
            "Improve productivity by setting daily goals and minimizing distractions."
        )

    if learning < 5:
        recommendations.append(
            "Increase learning hours. Try studying new skills or technologies daily."
        )

    if networking < 5:
        recommendations.append(
            "Build your professional network. Connect with industry professionals on LinkedIn."
        )

    if content < 5:
        recommendations.append(
            "Start sharing your knowledge through posts, blogs, or videos."
        )

    if health < 5:
        recommendations.append(
            "Maintain good health habits. Exercise regularly and get enough sleep."
        )

    if len(recommendations) == 0:
        recommendations.append(
            "Excellent! Your habits support strong personal brand growth."
        )

    return recommendations