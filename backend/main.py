from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
import uuid


app = FastAPI(
    title="NeuroTrace AI System",
    description="AI Observability System with FastAPI",
    version="1.0.0"
)


# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Temporary memory storage
logs = []

metrics = {
    "total_requests": 0,
    "success_count": 0,
    "error_count": 0,
    "total_latency": 0
}


@app.get("/")
async def home():
    return {
        "message": "NeuroTrace AI System Running 🚀",
        "status": "healthy"
    }



@app.post("/chat")
async def chat(data: dict):

    start_time = time.time()

    request_id = str(uuid.uuid4())

    user_input = data.get("input", "")


    metrics["total_requests"] += 1


    try:

        if not user_input:
            raise Exception("Invalid empty input")


        # Simulated AI response
        response = (
            f"AI Analysis completed for: {user_input}"
        )


        latency = round(
            time.time() - start_time,
            4
        )


        metrics["success_count"] += 1
        metrics["total_latency"] += latency


        log = {
            "request_id": request_id,
            "input": user_input,
            "response": response,
            "latency": latency,
            "status": "success"
        }


        logs.append(log)


        return log



    except Exception as error:


        latency = round(
            time.time() - start_time,
            4
        )


        metrics["error_count"] += 1


        log = {
            "request_id": request_id,
            "input": user_input,
            "error": str(error),
            "latency": latency,
            "status": "error"
        }


        logs.append(log)


        return log




@app.get("/metrics-summary")
async def metrics_summary():

    total = metrics["total_requests"]

    if total > 0:
        success_rate = (
            metrics["success_count"]
            /
            total
        ) * 100
    else:
        success_rate = 0


    return {
        "total_requests": total,
        "success_count": metrics["success_count"],
        "error_count": metrics["error_count"],
        "success_rate": round(success_rate, 2)
    }




@app.get("/logs")
async def get_logs():

    return logs[-10:]




@app.post("/run-demo")
async def run_demo():

    demo_queries = [
        "Explain AI",
        "What is observability?",
        "",
        "How does tracing work?"
    ]


    results = []


    for query in demo_queries:

        result = await chat(
            {
                "input": query
            }
        )

        results.append(result)


    return {
        "demo": "completed",
        "results": results
    }
