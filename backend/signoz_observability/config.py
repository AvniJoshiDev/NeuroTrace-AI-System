import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_NAME = os.getenv(
        "APP_NAME",
        "NeuroTrace AI System"
    )

    VERSION = "1.0.0"

    ENVIRONMENT = os.getenv(
        "ENVIRONMENT",
        "development"
    )


    # OpenTelemetry / SigNoz
    OTEL_ENDPOINT = os.getenv(
        "OTEL_ENDPOINT",
        "http://localhost:4318"
    )


    SERVICE_NAME = os.getenv(
        "SERVICE_NAME",
        "neurotrace-ai-service"
    )


settings = Settings()
