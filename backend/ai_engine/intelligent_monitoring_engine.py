from flask import Flask, render_template, jsonify
import random
import time
import threading

app = Flask(__name__)

metrics = {
    "total_requests": 0,
    "success": 0,
    "errors": 0,
    "logs": [],
    "start_time": time.time()
}

def generate_log():
    events = [
        ("INFO", "User request processed"),
        ("SUCCESS", "Data fetched successfully"),
        ("ERROR", "Database timeout error"),
        ("ERROR", "API rate limit exceeded"),
        ("SUCCESS", "Model inference success")
    ]

    event = random.choice(events)
    
    metrics["total_requests"] += 1

    if event[0] == "ERROR":
        metrics["errors"] += 1
    else:
        metrics["success"] += 1

    log_entry = {
        "type": event[0],
        "message": event[1],
        "time": time.strftime("%H:%M:%S")
    }

    metrics["logs"].insert(0, log_entry)

    if len(metrics["logs"]) > 20:
        metrics["logs"].pop()

def background_worker():
    while True:
        generate_log()
        time.sleep(2)

@app.route("/")
def home():
    return render_template("ai_dashboard_elite.html")

@app.route("/metrics")
def get_metrics():
    uptime = int(time.time() - metrics["start_time"])
    success_rate = (metrics["success"] / metrics["total_requests"] * 100) if metrics["total_requests"] else 0

    return jsonify({
        "total_requests": metrics["total_requests"],
        "success": metrics["success"],
        "errors": metrics["errors"],
        "success_rate": round(success_rate, 2),
        "logs": metrics["logs"],
        "uptime": uptime
    })

if __name__ == "__main__":
    threading.Thread(target=background_worker, daemon=True).start()
    app.run(debug=True)
