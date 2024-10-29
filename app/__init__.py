from flask import Flask
from .users.views import users_bp  # Імпортуємо наш Blueprint

def create_app():
    app = Flask(__name__)

    # Реєструємо Blueprint для користувачів з префіксом /users
    app.register_blueprint(users_bp, url_prefix='/users')

    return app
