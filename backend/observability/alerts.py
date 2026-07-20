"""
NeuroTrace Observability Engine
Alert Management Layer

Detects:
- High error rate
- Slow AI responses
- System degradation
"""


from datetime import datetime


alerts_history = []



def create_alert(
    alert_type: str,
    message: str,
    severity: str
):

    alert = {

        "timestamp":
            datetime.utcnow().isoformat(),

        "type":
            alert_type,

        "severity":
            severity,

        "message":
            message

    }


    alerts_history.append(alert)

    return alert




def check_error_alert(
    error_count: int,
    total_requests: int
):

    if total_requests == 0:
        return None


    error_rate = (
        error_count /
        total_requests
    ) * 100



    if error_rate > 30:

        return create_alert(
            alert_type="HIGH_ERROR_RATE",
            message=
            "AI system error rate crossed 30%",
            severity="critical"
        )


    elif error_rate > 10:

        return create_alert(
            alert_type="WARNING_ERROR_RATE",
            message=
            "AI system showing increased failures",
            severity="warning"
        )


    return None





def check_latency_alert(
    latency: float
):

    if latency > 3:

        return create_alert(
            alert_type="SLOW_RESPONSE",
            message=
            "AI response latency is high",
            severity="warning"
        )


    return None




def get_alerts():

    return alerts_history[-20:]
