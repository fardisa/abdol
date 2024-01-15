```python
from flask import Flask, request
import models
import middlewares
from utils import log_change, log_error
import routes
import controllers

app = Flask(__name__)

@app.before_request
def before_request():
    try:
        middlewares.auth_middleware(request)
        middlewares.request_logger(request)
    except Exception as e:
        log_error(str(e))
        raise e

@app.route('/')
def index():
    try:
        return controllers.index_controller()
    except Exception as e:
        log_error(str(e))
        raise e

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        log_error(str(e))
        raise e
```