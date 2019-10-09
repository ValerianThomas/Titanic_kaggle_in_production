# Titanic API REST
## Overview
Create an API that will tell if you would survived the accident or not based on the informations you provided.

## Functionality scope
### APP flow prediction
- - - -
* The user provides his data to the api 
* The data is sent as a post request to the api
* The api checks if all compulsory data are completed
* if not completed, the api replies to the user that he needs to provide complete informations 
* if completed, the api will pass the data into the model and returns the prediction
* bonus : the api saves the data entered and the prediction made in the databased as predicted_data

###  APP flow training
- - - -
	* The user launches the training of the model by making a request to the api.
	* the api receives the request.
	* the api pulls all the data related to the titanic passengers.
	* the api creates a DataFrame based the data pulled from the database.
	* the api passes the DataFrame to be fitted into the pipeline in order to create the model.
	* the api saves the model.
	* the api returns to the user that the model is saved.


##  Technical scope
For this project, you will need to do four differents steps:

### Step 1 Preprocessing
1.  Understand and preprocess the data in a Jupiter notebook.

### Step 2 Setup
1. From the train.csv, create a **database model** called Passengers ( pro tip, use each feature in your train.csv as a key in your Passengers Schema).

### Step 3 Pipeline Creation
1. Create your **prediction model** pipeline using the data coming from your database ( you will have to create a DataFrame based on the data you get from the database ).
2. Create the function that will train and save the pipeline model as a .sav file.

### Step 4 API Creation
1. Create a Flask api with two routes ( /train and /predict ).
2. Put everything together ;)







