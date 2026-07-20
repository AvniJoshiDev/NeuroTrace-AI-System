from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor

def setup_tracing():
    resource = Resource.create({
        "service.name": "neurotrace-ai-system"
    })

    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    exporter = OTLPSpanExporter(
        endpoint="http://signoz:4317",
        insecure=True
    )

    span_processor = BatchSpanProcessor(exporter)
    provider.add_span_processor(span_processor)

    return trace.get_tracer(__name__)
