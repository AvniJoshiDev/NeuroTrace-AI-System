def check_system_health(metrics):
    alerts = []

    if metrics.get("errors", 0) > 10:
        alerts.append("🚨 Critical Alert: High error rate")

    if metrics.get("latency", 0) > 2:
        alerts.append("⚠️ High latency detected")

    return alerts
