---
title: Diabetes Risk Ai
emoji: 🏥
colorFrom: pink
colorTo: indigo
sdk: streamlit
app_file: app.py
python_version: 3.11
pinned: false
---

# Diabetes Risk Predictor

A Streamlit web app that estimates diabetes risk from a handful of clinical measurements, using a Random Forest classifier.

> **Educational use only.** This is a learning project and not a medical device. It does not provide medical advice or diagnosis.

## How it works

1. Set the sliders for glucose level, BMI, age, blood pressure, and number of pregnancies.
2. Click **Analyze Risk**.
3. The model returns a high or low risk result with its probability.

Skin thickness, insulin, and diabetes pedigree function are not collected in the UI. The app uses fixed default values for them (0, 0, and 0.5).

## Run locally

```bash
git clone https://github.com/Marouane2005/diabetes-risk-ai.git
cd diabetes-risk-ai
pip install -r requirements.txt
streamlit run app.py
```

## Project files

- `app.py`: the Streamlit interface and prediction logic
- `diabetes_model.pkl`: the trained Random Forest model
- `requirements.txt`: pinned dependencies (scikit-learn 1.6.1, joblib 1.4.2)

## Tech stack

Python, Streamlit, scikit-learn, pandas, joblib

## License

Released under the [MIT License](LICENSE).
