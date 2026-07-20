"""
NeuroTrace Observability Engine

OpenTelemetry Tracing Layer
Exports traces to SigNoz using OTLP
"""


import os

from opentelemetry import trace

from opentelemetry.sdk.trace import (
    TracerProvider
)

from opentelemetry.sdk.resources import (
    Resource
)

from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor
)

from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
    OTLPSpanExporter
)



SERVICE_NAME = os.getenv(
    "SERVICE_NAME",
    "neurotrace-ai-system"
)


OTLP_ENDPOINT = os.getenv(
    "OTEL_EXPORTER_OTLP_ENDPOINT",
    "http://localhost:4318/v1/traces"
)



resource = Resource.create(
    {
        "service.name": SERVICE_NAME,
        "service.version": "1.0.0",
        "deployment.environment": "hackathon"
    }
)



provider = TracerProvider(
    resource=resource
)



exporter = OTLPSpanExporter(
    endpoint=OTLP_ENDPOINT
)



processor = BatchSpanProcessor(
    exporter
)



provider.add_span_processor(
    processor
)



trace.set_tracer_provider(
    provider
)



tracer = trace.get_tracer(
    "neurotrace-ai"
)



def create_span(name: str):

    return tracer.start_as_current_span(
        name
    )
