"""
NeuroTrace Observability Engine

OpenTelemetry Metrics Layer
Exports AI system metrics to SigNoz
"""


import os


from opentelemetry import metrics

from opentelemetry.sdk.metrics import (
    MeterProvider
)

from opentelemetry.sdk.resources import (
    Resource
)

from opentelemetry.sdk.metrics.export import (
    PeriodicExportingMetricReader
)

from opentelemetry.exporter.otlp.proto.http.metric_exporter import (
    OTLPMetricExporter
)



SERVICE_NAME = os.getenv(
    "SERVICE_NAME",
    "neurotrace-ai-system"
)



OTLP_ENDPOINT = os.getenv(
    "OTEL_EXPORTER_OTLP_METRICS_ENDPOINT",
    "http://localhost:4318/v1/metrics"
)



resource = Resource.create(
    {
        "service.name": SERVICE_NAME,
        "service.version": "1.0.0"
    }
)



metric_exporter = OTLPMetricExporter(
    endpoint=OTLP_ENDPOINT
)



reader = PeriodicExportingMetricReader(
    metric_exporter
)



provider = MeterProvider(
    resource=resource,
    metric_readers=[
        reader
    ]
)



metrics.set_meter_provider(
    provider
)



meter = metrics.get_meter(
    "neurotrace-ai"
)



# Total AI requests

total_requests = meter.create_counter(
    name="ai_requests_total",
    description="Total AI requests processed"
)



# Total errors

total_errors = meter.create_counter(
    name="ai_errors_total",
    description="Total AI failures"
)



# Response latency

request_latency = meter.create_histogram(
    name="ai_response_latency_seconds",
    description="AI response latency"
)



# Successful requests

successful_requests = meter.create_counter(
    name="ai_success_total",
    description="Successful AI responses"
)
