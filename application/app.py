from flask import Flask

from application.models import Senior
from .configuration import config
from .extensions import flask_db, login_manager

app = Flask(__name__)

def create_app(config_name):
    """Creates the app."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    configure_extensions(app)
    configure_blueprints(app)

    return app


def configure_extensions(app):
    """Configures the extensions."""

    flask_db.init_app(app)

    login_manager.session_protection = 'strong'
    login_manager.login_view = 'login'  # 指定了用户没有登录时，转跳那个视图进行登录，这里就是转跳login视图登录。
    login_manager.login_message = u'请登录'  # 没有登录时flash提示用户的消息
    login_manager.login_message_category = 'error'  # 没有登录时flash提示用户的消息的类别是error类型
    login_manager.needs_refresh_message = u'请重新登录'
    login_manager.needs_refresh_message_category = 'error'  # 需要重新登录时的flash提示消息

    @login_manager.user_loader
    def load_user(id):
        return Senior.get_or_none(Senior.id == id)


def configure_blueprints(app):
    from .misc import bp_misc
    app.register_blueprint(bp_misc, url_prefix='/misc')

    from .senior import bp_senior
    app.register_blueprint(bp_senior, url_prefix='/senior')

    from .welcome import bp_welcome
    app.register_blueprint(bp_welcome, url_prefix='/welcome')
