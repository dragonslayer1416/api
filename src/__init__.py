from flask import Flask

# Routes
from .routes import AuthRoutes
from .routes import CompaniesRoutes



app = Flask(__name__)


def init_app(config):
    # Configuration
    app.config.from_object(config)

    # Blueprints
    app.register_blueprint(AuthRoutes.main, url_prefix='/auth')
    app.register_blueprint(CompaniesRoutes.main, url_prefix='/companies')
    
   

    return app
