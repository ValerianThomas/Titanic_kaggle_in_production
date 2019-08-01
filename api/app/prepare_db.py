import os
import pandas as pd
from sqlalchemy import create_engine

TRAIN_CSV = os.path.dirname(os.path.realpath(__file__)) + '/prediction_model/data/train.csv'


def create_db():
  data = pd.read_csv(TRAIN_CSV)
  engine = create_engine(os.environ['DATABASE_URL'])
  return data.to_sql('passengers', engine)