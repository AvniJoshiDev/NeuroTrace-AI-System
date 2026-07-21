def explain_bug(log):
    msg = log.lower()

    if "timeout" in msg:
        return "Database timeout usually happens due to slow queries or server overload."

    elif "rate limit" in msg:
        return "API rate limit exceeded. Reduce request frequency."

    elif "invalid" in msg:
        return "Invalid input detected. Check request data format."

    return "Unknown issue detected. Needs deeper investigation."
