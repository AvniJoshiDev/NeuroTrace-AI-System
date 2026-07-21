import random

def detect_anomalies(metrics):
    anomalies = []

    error_rate = (metrics["errors"] / metrics["total_requests"]) if metrics["total_requests"] else 0

    if error_rate > 0.3:
        anomalies.append("🚨 High anomaly detected: Error spike!")

    if random.random() > 0.95:
        anomalies.append("⚠️ Sudden traffic spike detected!")

    return anomalies
