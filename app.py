def get_system_status(total, errors):
    error_rate = (errors / total) * 100 if total > 0 else 0

    if error_rate < 20:
        status = "GOOD"
        insight = "AI Insight: System performing optimally ✅"
    elif error_rate < 50:
        status = "WARNING"
        insight = "AI Insight: System needs attention ⚠️"
    else:
        status = "CRITICAL"
        insight = "AI Insight: System instability detected 🚨"

    return status, insight
