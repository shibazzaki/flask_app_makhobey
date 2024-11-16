from flask import Flask, render_template

def create_app(config_name="config"):
    app = Flask(__name__)
    app.config.from_object(config_name)  # Налаштування з конфігурації

    # Реєстрація Blueprint'ів
    from .posts import post_bp
    from .users import bp as user_bp
    app.register_blueprint(post_bp)
    app.register_blueprint(user_bp, url_prefix="/users")

    # Імпорт views
    with app.app_context():
        from . import views

    # Обробник помилки 404
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    return app
