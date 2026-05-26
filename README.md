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
- PostgreSQL for storage 

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
git clone https://github.com/yourusername/network-anomaly-detection.git
cd network-anomaly-detection
```

## Run Airflow services
docker-compose up 
## Start FastAPI backend
Uvicorn api :app –reload
## Open FastAPI documentation
http://localhost:8000/docs
## Launch Streamlit dashboard
streamlit run dashboard/app.py
## Open dashboard
http://localhost:8501
