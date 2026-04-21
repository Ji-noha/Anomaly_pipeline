import streamlit as st
import sqlite3
import pandas as pd
import os

st.title("Anomaly Dashboard")

# path to SAME DB used by Airflow
DB_PATH = os.path.abspath("data/db.sqlite3")

# connect
try:
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM logs", conn)
    conn.close()

    st.success("Database loaded successfully ✅")

    st.write("#--Raw Logs--#")
    st.dataframe(df)

    # simple visualization
    if not df.empty:
        st.write("#-- Requests per IP --#")
        st.bar_chart(df["ip"].value_counts())

except Exception as e:
    st.error(f"Error: {e}")