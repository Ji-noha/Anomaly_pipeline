# Anomaly_pipeline
# Network Anomaly Detection System — README Structure

```md
# Network Anomaly Detection System

## Overview

This project is an end-to-end anomaly detection platform designed for monitoring network traffic and identifying suspicious activities using machine learning.

The system processes network logs, performs feature engineering, trains an Isolation Forest anomaly detection model, exposes prediction services through FastAPI, and visualizes results using Streamlit dashboards.

Workflow orchestration is automated using Apache Airflow, and the entire infrastructure is containerized with Docker.

The project was built to combine machine learning, backend APIs, orchestration, and MLOps concepts into a practical system.

---

## Architecture

Network Logs → Data Processing → Feature Engineering → Isolation Forest Model → FastAPI Backend → Streamlit Dashboard

Additional Infrastructure:
- Apache Airflow for workflow orchestration
- Docker for containerization 

---

## Features

- Network log preprocessing pipeline
- Feature engineering for anomaly detection
- Isolation Forest machine learning model
- REST API using FastAPI
- Interactive Streamlit dashboard
- Apache Airflow DAG automation
- Dockerized deployment
- Modular project architecture

---

## Tech Stack

### Languages
- Python
- SQL
- Bash

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Backend
- FastAPI

### Visualization
- Streamlit

### Orchestration
- Apache Airflow

### Infrastructure
- Docker
- Docker Compose

---

## Installation

### Clone repository

```bash
git clone https://github.com/Ji-noha/Anomaly_pipeline
cd network-anomaly-detection
```

## Run Airflow services
docker-compose up 

<img width="1898" height="838" alt="image" src="https://github.com/user-attachments/assets/3950678f-98be-429b-9185-7ea9d63ea94c" />

## Start FastAPI backend
Uvicorn api :app –reload
## Open FastAPI documentation
http://localhost:8000/docs

<img width="1662" height="762" alt="image" src="https://github.com/user-attachments/assets/63a4ef58-8ebb-4a89-8783-410f939b112b" />

## Launch Streamlit dashboard
Streamlit run dashboard/dashboard.py
## Open dashboard
http://localhost:8501

<img width="1087" height="735" alt="image" src="https://github.com/user-attachments/assets/6cc36fea-4f39-4397-b5b1-86ebfed0c3c7" />

<img width="1015" height="507" alt="image" src="https://github.com/user-attachments/assets/54837f16-bf6e-48f0-b217-e91bbc4dad67" />
