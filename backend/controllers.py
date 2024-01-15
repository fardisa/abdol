```python
from flask import Blueprint, request
from .models import Model
from .middlewares import auth_middleware, error_handler, request_logger
from utils import log_change, log_error

controller = Blueprint('controller', __name__)

@controller.route('/update', methods=['POST'])
@auth_middleware
@request_logger
def update_code():
    try:
        data = request.get_json()
        model = Model.query.get(data['id'])
        model.code = data['code']
        model.save()
        log_change(f"Updated code for model {data['id']}")
        return {'message': 'Code updated successfully'}, 200
    except Exception as e:
        log_error(f"Error updating code for model {data['id']}: {str(e)}")
        return {'message': 'Error updating code'}, 500

@controller.route('/review', methods=['GET'])
@auth_middleware
@request_logger
def review_code():
    try:
        models = Model.query.all()
        for model in models:
            if not model.is_valid():
                log_error(f"Code for model {model.id} is not valid")
                return {'message': f"Code for model {model.id} is not valid"}, 400
        log_change("All codes reviewed and are valid")
        return {'message': 'All codes are valid'}, 200
    except Exception as e:
        log_error(f"Error reviewing codes: {str(e)}")
        return {'message': 'Error reviewing codes'}, 500
```