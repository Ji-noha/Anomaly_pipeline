import random
from datetime import datetime
import requests
import time
import os
import pandas as pd
from sklearn.ensemble import IsolationForest
import sqlite3


DB_PATH = "/opt/airflow/data/db.sqlite3"

def generate_ip():
    return f"192.168.{random.randint(0,255)}.{random.randint(1,254)}"

attack_ip = "192.168.1.100"

def generate_log(**kwargs):
    ports_normal =[80, 443]
    ports_attack= [22,23,3389,4444]

    attack_type = "None"
    rand= random.random() # trafic
    
    # ATTACK brute force 5% :
    if rand < 0.05:
        ip = attack_ip
        port = 22
        attack_type= "brute_force"

    # ATTACK port scanning 5% :
    elif rand< 0.10:
        ip= attack_ip
        port= random.randint(20,1024) # ports multiples
        attack_type= "port_scan"
    
    # Trafic normal 90 % :
    else:
        ip =generate_ip()
        port=random.choice(ports_normal)
        attack_type= "normal"

    log ={
        "ip": ip,
        "port": port,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "bytes": random.randint(200,5000),
        "protocol": "TCP",
        "attack_type": attack_type
    }

    return log

def ingestion(**kwargs): 
    for _ in range(50): 
        log = generate_log()

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            port INTEGER,
            timestamp TEXT,
            bytes INTEGER,
            protocol TEXT,
            attack_type TEXT
        )
        """)

        cur.execute("""
            INSERT INTO logs (ip, port, timestamp, bytes, protocol, attack_type)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            log["ip"],
            log["port"],
            log["timestamp"],
            log["bytes"],
            log["protocol"],
            log["attack_type"]
        ))

        conn.commit()
        conn.close()
        print("Inserted:", log)


def features(**kwargs):
    # connexion DB
    conn = sqlite3.connect(DB_PATH)

    df = pd.read_sql("SELECT * FROM logs", conn)

    conn.close()

    # nettoyage
    df = df.dropna()
    df["port"] = pd.to_numeric(df["port"], errors="coerce")
    df["bytes"] = pd.to_numeric(df["bytes"], errors="coerce")
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    df = df.dropna().drop_duplicates()

    # feature engineering
    features_df = df.groupby("ip").agg({
        "port": "nunique",
        "bytes": "sum",
        "timestamp": "count"
    }).reset_index()

    features_df.columns = [
        "ip",
        "unique_ports",
        "total_bytes",
        "request_count"
    ]

    # ML
    X = features_df[[
        "unique_ports",
        "total_bytes",
        "request_count"
    ]]

    model = IsolationForest(contamination=0.05, random_state=42)
    features_df["anomaly"] = model.fit_predict(X)
    features_df["anomaly"] = features_df["anomaly"].map({1: 0, -1: 1})

    print(features_df["anomaly"].value_counts())

    return features_df.to_dict()

