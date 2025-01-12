from flask import Flask, request, jsonify, render_template
from joblib import load
import numpy as np

model = load('multi_rf_model.joblib')

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_data = data['input']

        if len(input_data) != 22:
            return jsonify({'error': 'Invalid input size. Expected 22 features.'})
        input_array = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_array)
        response = {
            'predictions': {
                'Systolic Blood Pressure (mmHg)': prediction[0][0],
                'Diastolic Blood Pressure (mmHg)': prediction[0][1]
            }
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
