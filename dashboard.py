# dashboard.py

import streamlit as st
import pandas as pd

from regret_engine import calculate_brand_score, regret_risk
from analyzer import analyze_behavior
from recommendation import generate_recommendations
from database import create_table, save_record, get_all_records

# create database table
create_table()

st.title("🚀 Lets Build A Brand Of Yourself")

st.write("AI system that analyzes your habits and predicts personal brand growth.")

st.subheader("Enter Your Daily Habits")

productivity = st.slider("Productivity Level", 1, 10)
learning = st.slider("Learning Hours", 1, 10)
networking = st.slider("Networking Activity", 1, 10)
content = st.slider("Content Creation", 1, 10)
health = st.slider("Health & Fitness", 1, 10)

if st.button("Analyze My Brand Growth"):

    # calculate score
    score = calculate_brand_score(productivity, learning, networking, content, health)

    # calculate risk
    risk = regret_risk(score)

    # analyze behavior
    insights = analyze_behavior(productivity, learning, networking, content, health)

    # generate recommendations
    recommendations = generate_recommendations(productivity, learning, networking, content, health)

    # save data
    save_record(productivity, learning, networking, content, health, score, risk)

    st.subheader("📊 Brand Score")
    st.write(score)

    st.subheader("⚠ Future Regret Risk")
    st.write(risk)

    st.subheader("🔍 Behavior Insights")

    for insight in insights:
        st.write("-", insight)

    st.subheader("💡 Recommendations")

    for rec in recommendations:
        st.write("-", rec)


# ---------- Analytics Section ----------

st.subheader("📈 Brand Growth Analytics")

records = get_all_records()

if records:

    df = pd.DataFrame(records, columns=[
        "id",
        "productivity",
        "learning",
        "networking",
        "content",
        "health",
        "brand_score",
        "regret_risk"
    ])

    st.line_chart(df["brand_score"])

    st.write("Historical Data")
    st.dataframe(df)

else:

    st.write("No data available yet. Start analyzing your habits.")