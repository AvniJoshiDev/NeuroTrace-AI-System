"""
NeuroTrace Observability Engine
AI System Health Score Calculator

Calculates:
- Overall system health
- Status level
- Performance insights
"""


def calculate_health_score(
    total_requests: int,
    error_count: int,
    avg_latency: float
):

    score = 100


    # Error impact
    if total_requests > 0:

        error_rate = (
            error_count /
            total_requests
        ) * 100


        if error_rate > 30:
            score -= 40

        elif error_rate > 10:
            score -= 20


    # Latency impact

    if avg_latency > 5:

        score -= 30

    elif avg_latency > 2:

        score -= 15



    # Prevent negative score

    if score < 0:
        score = 0



    # System status

    if score >= 85:

        status = "Healthy"

    elif score >= 60:

        status = "Warning"

    else:

        status = "Critical"



    return {

        "health_score": score,

        "status": status,

        "message":
            f"System health is {status}",

        "recommendation":
            get_recommendation(status)

    }




def get_recommendation(status):


    if status == "Healthy":

        return (
            "System operating normally. "
            "Continue monitoring through SigNoz."
        )


    if status == "Warning":

        return (
            "Investigate latency and "
            "error patterns."
        )


    return (
        "Immediate investigation required. "
        "Check traces, logs and metrics in SigNoz."
    )
