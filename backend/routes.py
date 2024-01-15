```python
from flask import Flask, request
from controllers import *
from middlewares import auth_middleware, error_handler, request_logger
from utils import log_change, log_error

app = Flask(__name__)

@app.route('/')
@auth_middleware
@request_logger
def home():
    try:
        return main_controller.home()
    except Exception as e:
        log_error('ERROR.md', str(e))
        return error_handler(e)

@app.route('/update', methods=['POST'])
@auth_middleware
@request_logger
def update():
    try:
        data = request.get_json()
        result = main_controller.update(data)
        log_change('LOG.md', 'Update operation performed')
        return result
    except Exception as e:
        log_error('ERROR.md', str(e))
        return error_handler(e)

if __name__ == "__main__":
    app.run(debug=True)
```