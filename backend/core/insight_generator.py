def generate_insight(error_rate: float, latency: float, request_count: int):
    
    insights = []

    if error_rate > 0.5:
        insights.append("🚨 Critical: High error rate detected.")
    elif error_rate > 0.2:
        insights.append("⚠️ Warning: Errors are increasing.")

    if latency > 2:
        insights.append("🐢 Slow response detected (high latency).")

    if request_count > 100:
        insights.append("🔥 High traffic load on system.")

    if not insights:
        return "✅ System stable. No anomalies detected."

    return " | ".join(insights)
