from flask import Flask, request, jsonify 
from . import db
from .config import app_config
from .routes.product import product_end_point as product_blueprint
from .routes.prediction import prediction_api as prediction_blueprint
import os

# init app db marshmallow
def create_app():
  app = Flask(__name__)
  app.config.from_object(app_config['development'])
  db.init_app(app)

  app.register_blueprint(product_blueprint, url_prefix='/product')
  app.register_blueprint(prediction_blueprint, url_prefix='/prediction')
  return app

# migration manager



# run server 
if __name__ == '__main__':
  app.run(debug=True)