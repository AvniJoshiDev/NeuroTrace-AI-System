def calculate_health(metrics):
    if metrics["total_requests"] == 0:
        return 100

    success_rate = metrics["success"] / metrics["total_requests"]

    health_score = int(success_rate * 100)

    return health_score
