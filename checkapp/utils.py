import re

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