from flask import Flask

api = Flask(__name__)

from api.routes import api_bp

api.register_blueprint(api_bp)