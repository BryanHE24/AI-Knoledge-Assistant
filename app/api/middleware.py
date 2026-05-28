import time
import uuid
import logging

from fastapi import Request

logger = logging.getLogger(__name__) # Get the logger for the current module
    
# Middleware to log incoming requests
async def request_logging_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4()) # Generate a unique request ID
    start = time.time() # Record the start time

    response = await call_next(request) # Call the next middleware or route handler

    latency_ms = round((time.time() - start) * 1000, 2) # Calculate the response time in milliseconds

    # Log the request details
    logger.info(
        f"request_id={request_id} "
        f"method={request.method} "
        f"path={request.url.path} "
        f"status={response.status_code} "
        f"latency_ms={latency_ms}"
    )
    
    response.headers["X-Request-ID"] = request_id # Add the request ID to the response headers
    return response # Return the response