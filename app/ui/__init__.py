from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from app.data.db import session


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abc123'
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from app.data.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return session.query(User).get(user_id)

    CORS(app)

    from app.ui.routes import index
    app.register_blueprint(index.bp)

    from app.ui.routes import place
    app.register_blueprint(place.bp)

    from app.ui.routes import map
    app.register_blueprint(map.bp)

    from app.ui.routes import api
    app.register_blueprint(api.bp)

    from app.ui.routes import auth
    app.register_blueprint(auth.bp)

    from app.ui.routes import main
    app.register_blueprint(main.bp)

    app.add_url_rule('/', endpoint='index')

    return app
