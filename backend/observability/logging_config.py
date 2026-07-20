"""
NeuroTrace Observability Engine

Structured Logging Layer
JSON logs with Trace ID correlation
"""

import logging
import json
from datetime import datetime


from opentelemetry import trace



class JSONFormatter(
    logging.Formatter
):


    def format(self, record):


        span = trace.get_current_span()

        span_context = (
            span.get_span_context()
            if span
            else None
        )


        trace_id = None


        if span_context and span_context.is_valid:

            trace_id = format(
                span_context.trace_id,
                "032x"
            )



        log_data = {

            "timestamp":
                datetime.utcnow()
                .isoformat(),

            "level":
                record.levelname,

            "message":
                record.getMessage(),

            "service":
                "neurotrace-ai-system",

            "trace_id":
                trace_id

        }



        return json.dumps(
            log_data
        )





logger = logging.getLogger(
    "neurotrace"
)


logger.setLevel(
    logging.INFO
)



handler = logging.StreamHandler()



handler.setFormatter(
    JSONFormatter()
)



logger.addHandler(
    handler
)



def log_event(
    event_name,
    details
):


    logger.info(
        json.dumps(
            {
                "event": event_name,
                "details": details
            }
        )
    )



def log_error(
    error,
    details=None
):


    logger.error(
        json.dumps(
            {
                "error": str(error),
                "details": details
            }
        )
    )
