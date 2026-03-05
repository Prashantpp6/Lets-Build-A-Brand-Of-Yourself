# database.py

import sqlite3

# connect to database
conn = sqlite3.connect("brand_agent.db", check_same_thread=False)

cursor = conn.cursor()


def create_table():
    """
    Create database table if it doesn't exist
    """

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS brand_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        productivity INTEGER,
        learning INTEGER,
        networking INTEGER,
        content INTEGER,
        health INTEGER,
        brand_score REAL,
        regret_risk TEXT
    )
    """)

    conn.commit()


def save_record(productivity, learning, networking, content, health, score, risk):
    """
    Save a new record
    """

    cursor.execute(
        """
        INSERT INTO brand_data
        (productivity, learning, networking, content, health, brand_score, regret_risk)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (productivity, learning, networking, content, health, score, risk)
    )

    conn.commit()


def get_all_records():
    """
    Fetch all records
    """

    cursor.execute("SELECT * FROM brand_data")

    return cursor.fetchall()