from checkapp import validate_field


def test_validate_date_format1():
    assert validate_field("12.12.2024") == "date"

def test_validate_date_format2():
    assert validate_field("2024.12.12") == "text"
def test_validate_phone():
    assert validate_field("+7 123 456 78 90") == "phone"
def test_validate_phone1():
    assert validate_field("+71234567890") == "phone"
def test_validate_phone2():
    assert validate_field("+7 999 111 1111") == "phone"
def test_validate_phone3():
    assert validate_field("+7 123 4567890") == "phone"

def test_validate_email():
    assert validate_field("test@wow.com") == "email"

def test_validate_text():
    assert validate_field("Lorem ipsum") == "text"

def test_invalid_phone():
    assert validate_field("+7 123 456 78") == "text"  # Некорректный номер телефона

def test_invalid_email():
    assert validate_field("test.com") == "text"  # Некорректный email