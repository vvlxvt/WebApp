from flask import Blueprint, request, jsonify
import re
from .db import db
from .utils import validate_field

# Создаем Blueprint для маршрутов
routes = Blueprint("routes", __name__)

@routes.route("/get_form", methods=["POST"])
def get_form():
    data = request.form.to_dict()
    templates = db.all()

    for template in templates:
        all_fields_match = True
        for field in template["fields"]:
            if field not in data:
                all_fields_match = False
                break
            value_type = validate_field(data[field])
            expected_type = template["fields"].get(field)
            if value_type != expected_type:
                all_fields_match = False
                break
        if all_fields_match:
            return jsonify({"template_name": template["name"]})

    response = {field: validate_field(value) for field, value in data.items()}
    return jsonify(response)

@routes.errorhandler(500)
def internal_error(error):
    return jsonify({"status": "error", "message": "Internal Server Error"}), 500
