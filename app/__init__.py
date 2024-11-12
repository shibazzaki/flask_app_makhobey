from flask import Flask, render_template
from .posts import post_bp
from .users import bp as user_bp
import os

app = Flask(__name__)
app.config.from_pyfile("../config.py")
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(post_bp)
app.register_blueprint(user_bp, url_prefix="/users")

# Імпорт views після створення app
from . import views


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
