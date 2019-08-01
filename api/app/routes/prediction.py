from flask import request, jsonify, Response, Blueprint
from ..prediction_model.run_pipeline import train_pipeline
from ..prediction_model.make_prediction import make_prediction, test_prediction
prediction_api = Blueprint('prediction_api', __name__)

@prediction_api.route('/training', methods=['GET'])
def start_training ():
  try:
    train_pipeline()
    return jsonify({"success":True})
  except :
    return jsonify({"success":False, "error":"an error occur, check the log to see what happened"})

  
@prediction_api.route('/', methods=['POST'])
def make_new_prediction():
  req_data = request.get_json()
  try:
    prediction = make_prediction(req_data)
    return jsonify({"success":True, "prediction": prediction})
  except Exception as e:
    return jsonify({"success":False, "error":str(e)})

  
@prediction_api.route('/test', methods=['GET'])
def test_prediction_model():
  score = test_prediction()
  return jsonify({"success":True, "score": score})
