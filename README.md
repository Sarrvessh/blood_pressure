
# Blood Pressure Prediction Web App

This repository contains a Flask web application that predicts systolic and diastolic blood pressure based on several input features. The app uses a pre-trained multi-output regression model to make predictions.

## Features:
- Predicts systolic and diastolic blood pressure using a set of 22 input features.
- Built with Flask, a lightweight Python web framework.
- Uses `joblib` to load the pre-trained model for predictions.

## Prerequisites:
Before running the application, ensure you have the following installed:
- Python 3.6 or later
- pip (Python package manager)

## Setup Instructions:

1. Clone the repository:
   git clone https://github.com/yourusername/blood-pressure-prediction.git
   cd blood-pressure-prediction
   
2. Install the required dependencies:
  pip install -r requirements.txt

3.Run the Flask app:
  python app.py

4.Open the web app:
  Once the Flask app is running, open your browser and navigate to http://127.0.0.1:5000/ to access the prediction interface.

## Usage:
Input the data into the provided form for the following features:

Sex (M/F): Gender of the person (M for Male, F for Female).
Age (years): Age of the person.
Height (cm): Height of the person.
Weight (kg): Weight of the person.
Heart Rate (b/m): Heart rate in beats per minute.
BMI (kg/m²): Body Mass Index.
Hypertension (1/0): Whether the person has hypertension (1 for yes, 0 for no).
Diabetes (1/0): Whether the person has diabetes (1 for yes, 0 for no).
Cerebral Infarction (1/0): Whether the person has had a cerebral infarction (1 for yes, 0 for no).
Cerebrovascular Disease (1/0): Whether the person has cerebrovascular disease (1 for yes, 0 for no).
Segment 1-3: Segment features for input (numeric values).
Mean 1-3: Mean values for input (numeric values).
Variance 1-3: Variance values for input (numeric values).
Skewness 1-3: Skewness values for input (numeric values).
Click the "Predict" button to get the predicted systolic and diastolic blood pressure values.

## Example Output:
After submitting the form, the web app will display:

Systolic Blood Pressure (mmHg): Predicted systolic value.
Diastolic Blood Pressure (mmHg): Predicted diastolic value.

## Notes:
The app assumes that the pre-trained model is properly loaded and the input data is correctly formatted.
The input features must match the expected format and number (22 features) to work correctly with the model.
License:
This project is licensed under the MIT License - see the LICENSE file for details.
