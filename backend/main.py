from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
import uuid

from core.ai_engine import generate_ai_response
from core.error_analyzer import analyze_error
from core.failure_detector import check_failure_pattern

from models.schemas import ChatRequest

from observability.logging_config import logger
from observability.metrics import (
    total_requests,
    total_errors,
    request_latency
)

from middleware.request_tracker import RequestTracker


app = FastAPI(
    title="NeuroTrace AI System",
    description="AI Observability System with FastAPI + OpenTelemetry",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request tracking middleware
app.add_middleware(
    RequestTracker
)


logs = []


@app.get("/")
async def home():

    return {
        "message": "NeuroTrace AI System Running 🚀",
        "status": "healthy"
    }



@app.post("/chat")
async def chat(request: ChatRequest):

    start_time = time.time()

    request_id = str(uuid.uuid4())

    total_requests.add(1)


    try:

        response = await generate_ai_response(
            request.input
        )


        latency = round(
            time.time() - start_time,
            4
        )


        request_latency.record(
            latency
        )


        logs.append(
            {
                "request_id": request_id,
                "input": request.input,
                "response": response,
                "latency": latency,
                "status": "success"
            }
        )


        logger.info(
            {
                "trace": request_id,
                "status": "success",
                "latency": latency
            }
        )


        return {
            "request_id": request_id,
            "response": response,
            "latency": latency,
            "status": "success"
        }



    except Exception as error:


        total_errors.add(1)


        error_data = analyze_error(
            str(error)
        )


        latency = round(
            time.time() - start_time,
            4
        )


        logs.append(
            {
                "request_id": request_id,
                "error": error_data,
                "latency": latency,
                "status": "error"
            }
        )


        logger.error(
            {
                "trace": request_id,
                "error": error_data
            }
        )


        return {
            "request_id": request_id,
            "error": error_data,
            "latency": latency,
            "status": "error"
        }




@app.get("/logs")
async def get_logs():

    return logs[-10:]




@app.get("/metrics-summary")
async def metrics_summary():

    total = len(logs)

    success = len(
        [
            x for x in logs
            if x.get("status")=="success"
        ]
    )

    errors = total - success


    return {

        "total_requests": total,
        "success": success,
        "errors": errors,
        "success_rate":
            round(
                (success / total * 100)
                if total else 0,
                2
            )
    }




@app.get("/analysis-report")
async def analysis_report():

    return check_failure_pattern()




@app.post("/run-demo")
async def run_demo():

    examples = [
        "Explain AI",
        "What is observability?",
        "",
        "unclear xyz"
    ]


    results=[]


    for item in examples:

        result = await chat(
            ChatRequest(
                input=item
            )
        )

        results.append(result)


    return {
        "demo":"completed",
        "results":results
    }
