# 🚀 NeuroTrace AI System

## AI Observability Platform powered by FastAPI + OpenTelemetry + SigNoz


NeuroTrace AI System is a production-style AI monitoring platform that not only generates AI responses but also observes, analyzes, and explains system behavior.

The system tracks:

- AI Requests
- Response Latency
- Errors
- Logs
- Distributed Traces
- System Health
- Failure Patterns


---

# 🧠 Architecture


```text
User
 |
 |
Frontend Dashboard
 |
 |
FastAPI Backend
 |
 |
NeuroCore AI Engine
 |
 |
OpenTelemetry
 |
 |----------------|
 |                |
Traces          Metrics
 |                |
 |                |
Logs ----------> SigNoz
                  |
             Dashboard



# ⚡ Installation


## Clone Repository

git clone YOUR_REPOSITORY_URL

cd NeuroTrace-AI-System


## Install Backend Dependencies

cd backend

pip install -r requirements.txt


## Run FastAPI Backend

uvicorn main:app --reload


API:

http://localhost:8000


Swagger Documentation:

http://localhost:8000/docs



# 🐳 Run SigNoz Observability Stack


Start SigNoz:

docker-compose up -d


SigNoz Dashboard:

http://localhost:3301



# 📡 Observability Flow


AI Request

↓

FastAPI Backend

↓

NeuroCore AI Engine

↓

OpenTelemetry SDK

↓

OTLP Exporter

↓

OpenTelemetry Collector

↓

SigNoz Dashboard

↓

Insights & Monitoring
