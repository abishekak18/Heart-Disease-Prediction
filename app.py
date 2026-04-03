from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle
import json

app = Flask(__name__)

# load your trained model
model = pickle.load(open('model.pkl', 'rb'))

# Define the features for reference
FEATURES = {
    'age': {'label': 'Age', 'type': 'number', 'min': 0, 'max': 120, 'unit': 'years'},
    'sex': {'label': 'Sex', 'type': 'select', 'options': [('0', 'Female'), ('1', 'Male')]},
    'cp': {'label': 'Chest Pain Type', 'type': 'select', 'options': [('0', 'Typical Angina'), ('1', 'Atypical Angina'), ('2', 'Non-anginal Pain'), ('3', 'Asymptomatic')]},
    'trestbps': {'label': 'Resting Blood Pressure', 'type': 'number', 'min': 80, 'max': 200, 'unit': 'mmHg'},
    'chol': {'label': 'Serum Cholesterol', 'type': 'number', 'min': 100, 'max': 400, 'unit': 'mg/dl'},
    'fbs': {'label': 'Fasting Blood Sugar > 120', 'type': 'select', 'options': [('0', 'No'), ('1', 'Yes')]},
    'restecg': {'label': 'Resting ECG', 'type': 'select', 'options': [('0', 'Normal'), ('1', 'ST-T Abnormality'), ('2', 'LV Hypertrophy')]},
    'thalach': {'label': 'Max Heart Rate Achieved', 'type': 'number', 'min': 60, 'max': 200, 'unit': 'bpm'},
    'exang': {'label': 'Exercise Induced Angina', 'type': 'select', 'options': [('0', 'No'), ('1', 'Yes')]},
    'oldpeak': {'label': 'ST Depression', 'type': 'number', 'min': 0, 'max': 6, 'unit': 'mm', 'step': '0.1'},
    'slope': {'label': 'ST Slope', 'type': 'select', 'options': [('0', 'Upsloping'), ('1', 'Flat'), ('2', 'Downsloping')]},
    'ca': {'label': 'Number of Major Vessels', 'type': 'select', 'options': [('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')]},
    'thal': {'label': 'Thalassemia', 'type': 'select', 'options': [('1', 'Normal'), ('2', 'Fixed Defect'), ('3', 'Reversible Defect')]},
}

@app.route('/')
def home():
    return render_template('index.html', features=FEATURES)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        data = [float(request.form.get(key, 0)) for key in FEATURES.keys()]
        final_input = np.array(data).reshape(1, -1)

        # Get prediction and probability
        prediction = model.predict(final_input)[0]
        
        # Try to get probability if model supports it
        try:
            probability = model.predict_proba(final_input)[0]
            confidence = float(max(probability))
        except:
            confidence = None

        # Prepare result
        if prediction == 0:
            result = "No Heart Disease"
            risk_level = "Low Risk"
            color = "green"
        else:
            result = "Heart Disease Detected"
            risk_level = "High Risk"
            color = "red"

        # Create a visualization data structure
        viz_data = {
            'labels': list(FEATURES.keys()),
            'values': [float(v) for v in data],
            'prediction': int(prediction),
            'confidence': confidence
        }

        return render_template('index.html', 
                             prediction_text=result,
                             risk_level=risk_level,
                             color=color,
                             confidence=confidence,
                             viz_data=json.dumps(viz_data),
                             features=FEATURES)
    except Exception as e:
        return render_template('index.html', 
                             prediction_text=f"Error: {str(e)}",
                             features=FEATURES)

if __name__ == "__main__":
    app.run(debug=True)