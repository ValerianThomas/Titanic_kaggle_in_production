import os
import pickle
import pandas as pd 
MODEL_PATH = os.path.dirname(os.path.realpath(__file__)) + '/saved_models/model.sav'
TEST_CSV = os.path.dirname(os.path.realpath(__file__)) + '/data/test.csv'


def make_prediction(input_data):
  data = pd.DataFrame(input_data)
  model = pickle.load(open(MODEL_PATH,'rb'))
  return model.predict(data).tolist()

def test_prediction():
  data = pd.read_csv(TEST_CSV)
  X = data.drop('Survived',axis=1)
  y = data['Survived']
  model = pickle.load(open(MODEL_PATH,'rb'))
  return model.score(X,y)
