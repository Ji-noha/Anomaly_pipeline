from fastapi import FastAPI
import sqlite3
import pandas as pd
import os


app = FastAPI()

# DB_PATH = "data/db.sqlite3"
# DB_PATH= "C:/Users/user/pipeline_anomlay/airflow-projects/data/db.sqlite3"
# DB_PATH = os.path.join("data", "db.sqlite3")

"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "db.sqlite3")
"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "db.sqlite3")

@app.get("/anomalies")
def get_anomalies():
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql("SELECT * FROM logs", conn)

    conn.close()


    return df.tail(20).to_dict(orient="records")

####################################################
"""
from fastapi import FastAPI
import sqlite3
import pandas as pd
import os

app = FastAPI()

DB_PATH = "data/db.sqlite3"

@app.get("/anomalies")
def get_anomalies():
    try:
        print("DB exists:", os.path.exists(DB_PATH))

        conn = sqlite3.connect(DB_PATH)

        df = pd.read_sql("SELECT * FROM logs", conn)

        conn.close()

        print("Data shape:", df.shape)

        if df.empty:
            return {"message": "No data yet"}

        return df.tail(20).to_dict(orient="records")

    except Exception as e:
        return {"error": str(e)}

"""