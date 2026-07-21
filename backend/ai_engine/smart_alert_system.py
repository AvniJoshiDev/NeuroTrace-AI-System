def check_alerts(metrics):
    alerts = []

    if metrics["errors"] >= 5:
        alerts.append("High error rate detected!")

    if metrics["success_rate"] < 60:
        alerts.append("Low success rate warning!")

    return alerts
