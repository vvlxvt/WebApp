from flask import Flask
from .db import db
from .models import add_sample_data
from .routes import routes  # Импортируем маршруты

def create_app():
    app = Flask(__name__)

    # Добавление шаблонов в базу данных
    add_sample_data()

    # Регистрируем Blueprint
    app.register_blueprint(routes)

    return app
