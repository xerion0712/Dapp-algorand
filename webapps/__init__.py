from flask import Flask

from . import auth
from . import views


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "put any long random string here"

    auth.login_manager.init_app(app)

    app.register_blueprint(views.main_bp)
    app.register_blueprint(auth.auth_bp)

    return app
