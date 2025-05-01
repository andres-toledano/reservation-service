from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.config.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # Cargar la configuración
    config = Config()
    app.config.from_object(config)

    # Inicializar db y migraciones
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar Blueprints
    from src.controller.api_controller import reservation_bp
    app.register_blueprint(reservation_bp)

    return app
