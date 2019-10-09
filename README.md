# Kaggle Titanic model  in production with Flask and Docker
- - - -
This repository is a complete set-up to build the a gaggle Titanic model into production using Flask and Docker
[The scope of the project can be found here](./Scope.md)

## Dependencies
- - - -
Flask, Docker, Pandas, Scikit-learn, Postgres

## Workflow
- - - -
This app works in three steps:
First, using Pandas and Postgres, the application uses the Titanic dataset provided by Kaggle to pass it to the Postgres server as a new table called “passengers”.
Second, it will start the training pipeline using again Pandas but this time with Scikit-learn Pipeline class. Pandas pulls data from our server then transform to a dataframe that will pass through the pipeline.
Once done the pipleine saves the newly train model.
Third, the model is provided to the Flask for the world to consume.

## Set-up 
- - - -
In order to build, the docker container is expecting three env variables:
1. DATABASE_URL: the address of your Postgres database (ElephantSQL ? )
2. PORT: 5000 
3. SHOULD_FILL_DB: yes , this will let the application fills your database from the train.csv provided by Kaggle

### Exemple

``` bash
docker build -t titanic_model .
sudo DATABASE_URL=<your url> PORT=5000 SHOULD_FILL_DB=yes docker run titanic_model -e DATABASE_URL -e PORT -e SHOULD_FILL_DB -p 5000:5000 titanic_model
```

## Routes
- - - -
‘_prediction_training’
GET:
Trains the model from the data coming from a query 

‘_prediction_test’
GET:
Test the accuracy of the model based on a test set.

‘_prediction_‘
POST:
the body, requires a json of objects , for details about the key please check the Kaggle competition [https://www.kaggle.com/c/titanic/data](https://www.kaggle.com/c/titanic/data)
```
[{
"Pclass":3,
"Sex":"female",
"Age":22.0,
"SibSp":1,
"Parch":2,
"Fare":7.7500	,
"Embarked":"Q"	
}]

```
