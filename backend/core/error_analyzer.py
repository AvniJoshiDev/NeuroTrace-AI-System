def analyze_error(error_message: str):

    error = error_message.lower()


    if "empty" in error:
        return {
            "error_type": "invalid_input",
            "root_cause": "User provided empty input",
            "explanation": "AI engine received no usable data",
            "suggestion": "Provide a clear question or message"
        }


    if "timeout" in error:
        return {
            "error_type": "api_timeout",
            "root_cause": "AI model response took too long",
            "explanation": "The model service did not respond in time",
            "suggestion": "Retry request or increase timeout limit"
        }


    if "confusion" in error:
        return {
            "error_type": "model_confusion",
            "root_cause": "AI could not understand the request",
            "explanation": "Input pattern was unclear",
            "suggestion": "Rewrite the prompt with more details"
        }


    return {
        "error_type": "unknown_error",
        "root_cause": "Unexpected system failure",
        "explanation": error_message,
        "suggestion": "Check logs and retry"
    }
