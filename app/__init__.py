from .routes import app
from .models import db
from config import Config

def create_app():
    app.config.from_object(Config)

    db.init_app(app)

    return app