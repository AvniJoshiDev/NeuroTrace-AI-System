def predict_future(metrics):
    if metrics["total_requests"] == 0:
        return "No prediction available"

    avg_success = metrics["success"] / metrics["total_requests"]

    if avg_success > 0.7:
        return "📈 System likely to remain stable"
    else:
        return "⚠️ System may face instability soon"
