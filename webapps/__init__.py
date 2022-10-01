from flask import Flask

from . import admin_page
from . import views_pages


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "put any long random string here"

    admin_page.login_manager.init_app(app)

    app.register_blueprint(views_pages.main_bp)
    app.register_blueprint(admin_page.auth_bp)

    return app
