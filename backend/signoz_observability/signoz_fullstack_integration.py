from flask import Flask, request
import time

# OpenTelemetry imports
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Setup tracer provider
resource = Resource(attributes={
    "service.name": "ai-observability-dashboard"
})

provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

# SigNoz OTLP endpoint (local or cloud)
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)

span_processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(span_processor)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

tracer = trace.get_tracer(__name__)

@app.route("/")
def home():
    with tracer.start_as_current_span("home_request"):
        time.sleep(0.2)
        return "AI Observability Dashboard Running with SigNoz 🚀"

@app.route("/api")
def api():
    with tracer.start_as_current_span("api_call"):
        time.sleep(0.3)
        return {"status": "success"}
