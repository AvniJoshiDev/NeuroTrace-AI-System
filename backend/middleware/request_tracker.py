import time
import uuid
import logging

from starlette.middleware.base import BaseHTTPMiddleware


logger = logging.getLogger("neurotrace")


class RequestTracker(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        # Unique request ID
        request_id = str(uuid.uuid4())

        # Start time
        start_time = time.time()


        try:

            response = await call_next(request)

            status = "success"


        except Exception as error:

            status = "error"

            logger.error(
                {
                    "request_id": request_id,
                    "error": str(error)
                }
            )

            raise error



        # Calculate latency
        latency = round(
            time.time() - start_time,
            4
        )


        # Add tracking headers
        response.headers["X-Request-ID"] = request_id

        response.headers["X-Response-Time"] = str(latency)



        # Structured log
        logger.info(
            {
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "status": status,
                "latency": latency
            }
        )


        return response
