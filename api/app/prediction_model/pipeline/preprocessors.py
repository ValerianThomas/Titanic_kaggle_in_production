import numpy as np 
import pandas as pd 
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import power_transform
class Replace_nan_numerical_values(BaseEstimator, TransformerMixin):
  def __init__(self, features):
    if isinstance(features,list):
      self.features = features
    else:
      self.features = [features]
      
  def fit (self,X,y):
    return self

  def transform(self,X):
    X = X.copy()
    for feature in self.features:
      X[feature] = X[feature].fillna(X[feature].mode()[0])
    return X

class Replace_missing_categorical_data(BaseEstimator, TransformerMixin):
  def __init__(self,features):
    if isinstance(features,list):
      self.features = features
    else:
      self.features = [features]

  def fit(self,X,y):
    return self

  def transform(self,X):
    X = X.copy()
    for feature in self.features:
      X[feature]  =  X[feature].fillna( X[feature].value_counts().index[0])
    return X

class Delete_unused_features(BaseEstimator, TransformerMixin):
  def __init__(self,features):
    if isinstance(features,list):
      self.features = features
    else:
      self.features = [features]

  def fit(self,X,y):
    return self
  
  def transform(self,X):
    X = X.copy()
    for feature in self.features:
      if feature in X.columns:
        X = X.drop(feature,axis=1)
    return X

class Discrete_to_category(BaseEstimator, TransformerMixin):
  def __init__(self,features):
    if isinstance(features,list):
      self.features = features
    else:
      self.features = [features]
  
  def fit (self, X,y):
    return self

  def transform(self,X):
    X = X.copy()
    X[self.features] = X[self.features].astype('object')
    return X

class Normalizer (BaseEstimator, TransformerMixin):
  def __init__(self,features):
    if isinstance(features,list):
      self.features = features
    else:
      self.features = [features]
      
  
  def fit (self,X,y):
    return self

  def transform(self,X):
    X = X.copy()
    X[self.features] = power_transform( X[self.features], method='yeo-johnson')
    return X


class Rare_categories_detector(BaseEstimator, TransformerMixin):
  def __init__(self,features, indicator):
    if isinstance(features,list):
      self.features = features
    else:
      self.features = [features]
    self.indicator = indicator

  def fit (self,X,y):
    return self

  def transform(self,X):
    X = X.copy()
    for feature in self.features :
      X[feature] = np.where(X[feature].isin(self.indicator[feature]),X[feature], 'Rare')
      return X

class Get_dummies(BaseEstimator, TransformerMixin):
  
  def fit(self,X,y):
    X = X.copy()
    prev_columns = X.columns
    X = pd.get_dummies(X, drop_first=True)
    self.dummies = [feature for feature in X.columns if feature not in prev_columns ]
    return self

  def transform(self,X):
    X = X.copy()
    X = pd.get_dummies(X, drop_first=True)
    for feature in self.dummies:
      if feature not in X.columns:
        X[feature] = [0]*len(X.index)
    return X
