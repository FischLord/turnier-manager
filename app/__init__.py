from flask import Flask
from .extensions import db, migrate, login_manager
from .routes.main_routes import main
from .routes.event_routes import events
from .routes.participant_routes import participants
from .routes.result_routes import results
from .models.user import User

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(events)
    app.register_blueprint(participants)
    app.register_blueprint(results)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
