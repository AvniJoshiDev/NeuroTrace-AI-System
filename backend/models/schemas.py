from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    input: str = Field(
        ...,
        min_length=1,
        description="User message for AI"
    )


class AIResponse(BaseModel):
    request_id: str
    response: dict
    latency: float
    status: str


class ErrorResponse(BaseModel):
    request_id: str
    error: dict
    latency: float
    status: str
