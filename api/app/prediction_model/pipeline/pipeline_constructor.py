import numpy as np 
from sklearn.pipeline import Pipeline 
from sklearn.ensemble import RandomForestClassifier
from .preprocessors import Replace_nan_numerical_values, Replace_missing_categorical_data, Delete_unused_features, Discrete_to_category, Normalizer, Rare_categories_detector, Get_dummies
DISCRETE_VARS = [ 'Pclass', 'SibSp', 'Parch']
UNUSEDED_FEATURES = ['PassengerId','Cabin','Ticket','Name']
DISCRETE_TO_CAT = [ 'SibSp', 'Parch']
CONTINOUS = ['Age', 'Fare']
CATEGORIES = ['Sex','SibSp','Parch','Embarked']
NON_RARE_CATEGORIES = {
 'Sex': ['female', 'male'],
 'SibSp': [0, 1],
 'Parch': [0, 1, 2],
 'Embarked': ['C', 'Q', 'S']}

DUMMIES = [
'Sex_male',
'SibSp_1',
'Parch_1',
'Parch_2',
'Embarked_Q',
'Embarked_S'
]

prediction_pipeline = Pipeline([
('remove unused columns',Delete_unused_features(UNUSEDED_FEATURES)),
('replace nan in continous values', Replace_nan_numerical_values(CONTINOUS)),
('replace nan in categorical values', Replace_missing_categorical_data(CATEGORIES)),
('transform discrete values into categories',Discrete_to_category(DISCRETE_TO_CAT)),
('normalized continous values', Normalizer(CONTINOUS)),
('detect and remove rare categories', Rare_categories_detector(CATEGORIES, NON_RARE_CATEGORIES)),
('get the dummies',Get_dummies()),
('make model',RandomForestClassifier())
])