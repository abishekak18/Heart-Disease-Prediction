# CardioCheck - Heart Disease Risk Assessment

A modern, machine learning-powered web application for predicting heart disease risk. Built with Flask backend and a beautiful dark-themed UI with interactive visualizations.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Features

✨ **Modern UI/UX**
- Beautiful dark-themed interface with gradient accents
- Smooth animations and transitions
- Fully responsive design (desktop, tablet, mobile)
- Professional healthcare aesthetic

📊 **Interactive Visualizations**
- Risk distribution doughnut chart
- Patient parameter bar chart
- Real-time prediction confidence meter
- Dynamic result cards with color-coded risk levels

🤖 **Machine Learning**
- Pre-trained model predictions
- Confidence scoring
- 13 medical parameters for comprehensive analysis
- Instant predictions

🔒 **User-Friendly**
- Organized form with helpful hints
- Dropdown selections for categorical data
- Input validation and error handling
- Clear risk assessment results

## 📋 Requirements

```
Python 3.8+
Flask 2.0+
NumPy
Scikit-learn (or any ML framework your model uses)
Chart.js (included via CDN)
Plus Jakarta Sans font (included via Google Fonts)
```

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/abishekak18/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
```

### Step 2: Create a Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install flask numpy scikit-learn
```

### Step 4: Project Structure
Ensure your project has the following structure:
```
cardiocheck/
├── app.py
├── model.pkl
├── requirements.txt
└── templates/
    └── index.html
```

### Step 5: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 📁 File Descriptions

### `app.py`
Main Flask application file containing:
- Route definitions (`/` and `/predict`)
- Model loading from `model.pkl`
- Feature definitions with metadata
- Prediction logic
- Result formatting

### `templates/index.html`
Frontend interface with:
- HTML structure for the prediction form
- CSS styling (dark theme, animations, responsive design)
- JavaScript for form handling and Chart.js visualizations
- Jinja2 templating for dynamic form generation

### `model.pkl`
Pre-trained machine learning model for heart disease prediction. Should be a scikit-learn model with `predict()` and optionally `predict_proba()` methods.

## 📊 Input Features

The application analyzes 13 medical parameters:

| Feature | Type | Range | Unit |
|---------|------|-------|------|
| Age | Number | 0-120 | years |
| Sex | Select | 0-1 | (0=Female, 1=Male) |
| Chest Pain Type | Select | 0-3 | (0=Typical Angina, 1=Atypical, 2=Non-anginal, 3=Asymptomatic) |
| Resting Blood Pressure | Number | 80-200 | mmHg |
| Serum Cholesterol | Number | 100-400 | mg/dl |
| Fasting Blood Sugar | Select | 0-1 | (0=No, 1=Yes) |
| Resting ECG | Select | 0-2 | (0=Normal, 1=ST-T Abnormality, 2=LV Hypertrophy) |
| Max Heart Rate | Number | 60-200 | bpm |
| Exercise Induced Angina | Select | 0-1 | (0=No, 1=Yes) |
| ST Depression | Number | 0-6 | mm |
| ST Slope | Select | 0-2 | (0=Upsloping, 1=Flat, 2=Downsloping) |
| Major Vessels Count | Select | 0-3 | vessels |
| Thalassemia | Select | 1-3 | (1=Normal, 2=Fixed Defect, 3=Reversible) |

## 🎨 Customization

### Change Colors
Edit the CSS variables in `templates/index.html`:
```css
:root {
    --primary: #FF6B6B;        /* Red accent */
    --accent: #4ECDC4;         /* Teal accent */
    --success: #2ECC71;        /* Green for low risk */
    --bg-dark: #0A0E27;        /* Background */
}
```

### Update Feature Definitions
Edit the `FEATURES` dictionary in `app.py`:
```python
FEATURES = {
    'age': {'label': 'Age', 'type': 'number', 'min': 0, 'max': 120, 'unit': 'years'},
    # ... more features
}
```



## 📚 Model Information

This application uses a pre-trained machine learning model. The model should:
- Accept input shape: `(1, 13)` - one sample with 13 features
- Have a `predict()` method returning 0 (no disease) or 1 (disease)
- Optionally have `predict_proba()` for confidence scores

