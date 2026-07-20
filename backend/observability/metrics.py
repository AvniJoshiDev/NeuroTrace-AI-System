from opentelemetry import metrics


meter = metrics.get_meter(
    "neurotrace"
)


total_requests = meter.create_counter(
    "ai_requests_total",
    description="Total AI requests"
)


total_errors = meter.create_counter(
    "ai_errors_total",
    description="Total AI errors"
)


request_latency = meter.create_histogram(
    "ai_request_latency",
    description="AI response latency"
)
