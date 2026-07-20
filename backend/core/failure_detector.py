from datetime import datetime


failure_history = []


def record_failure(error_type):

    failure_history.append(
        {
            "type": error_type,
            "time": datetime.utcnow().isoformat()
        }
    )


def check_failure_pattern():

    total_failures = len(failure_history)


    if total_failures == 0:

        return {
            "health_score": 100,
            "status": "healthy",
            "message": "No failures detected"
        }


    if total_failures < 3:

        return {
            "health_score": 85,
            "status": "warning",
            "message": "Minor failures detected",
            "failures": failure_history
        }


    return {
        "health_score": 50,
        "status": "critical",
        "message": "High failure pattern detected",
        "failures": failure_history
    }
