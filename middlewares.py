```python
from utils import log_error, log_change

def auth_middleware(request, response, next):
    try:
        # Authentication logic here
        # If authenticated, call next()
        # Else, return error response
        pass
    except Exception as e:
        log_error('ERROR.md', f'Error in auth_middleware: {str(e)}')
        raise e

def error_handler(request, response, next):
    try:
        # Error handling logic here
        # If error, log it and return error response
        # Else, call next()
        pass
    except Exception as e:
        log_error('ERROR.md', f'Error in error_handler: {str(e)}')
        raise e

def request_logger(request, response, next):
    try:
        # Log the request details
        log_change('LOG.md', f'Request details: {request}')
        # Call next middleware or final route handler
        next()
    except Exception as e:
        log_error('ERROR.md', f'Error in request_logger: {str(e)}')
        raise e
```