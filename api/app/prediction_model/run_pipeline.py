import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from .pipeline.pipeline_constructor import prediction_pipeline

TRAINING_DATA_FILE = os.path.dirname(os.path.realpath(__file__)) + '/data/train.csv'
TESTING_DATA_FILE = os.path.dirname(os.path.realpath(__file__)) + '/data/test.csv'
MODEL_PATH = os.path.dirname(os.path.realpath(__file__)) + '/saved_models/model.sav'

def save_model(model):
  pickle.dump(model,open(MODEL_PATH,'wb'))

def train_pipeline():
  data = pd.read_csv(TRAINING_DATA_FILE)
  X = data.drop('Survived', axis=1)
  y = data['Survived']
  prediction_pipeline.fit(X,y)
  save_model(prediction_pipeline)
