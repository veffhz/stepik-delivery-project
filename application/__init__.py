from flask import Flask

from config import Config
from application.extensions import db, migrate, csrf
from application.extensions import login_manager, admin_manager


app = Flask(__name__)


def create_app(config_class=Config):
    app.config.from_object(config_class)
    from application.models import db, User
    from application.admin import init_admin
    from application import forms, processors, filters
    from application import controllers
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    admin_manager.init_app(app)
    init_admin(admin_manager)
    authentication(User)
    return app


def authentication(user_model):
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(uid):
        return user_model.query.get(uid)
