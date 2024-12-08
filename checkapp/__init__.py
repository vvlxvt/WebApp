from flask import Flask, request, jsonify
import re
from .db import db
from .models import add_sample_data

EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
PHONE_REGEX = r'^\+7\s?(\d{3})\s?(\d{3})\s?(\d{2})\s?(\d{2})$'
DATE_REGEX1 = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$"
DATE_REGEX2 = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"

def validate_field(value):
    """Функция для валидации поля."""
    if re.match(DATE_REGEX1, value) or re.match(DATE_REGEX2, value):
        return "date"
    elif re.match(PHONE_REGEX, value):
        return "phone"
    elif re.match(EMAIL_REGEX, value):
        return "email"
    else:
        return "text"

def create_app():
    app = Flask(__name__)

    # Добавление шаблонов в бд
    add_sample_data()

    @app.route("/get_form", methods=["POST"])
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

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"status": "error", "message": "Internal Server Error"}), 500

    return app
