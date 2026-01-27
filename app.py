import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load('diabetes_model.pkl')

st.set_page_config(page_title="Diabetes AI", page_icon="🏥")

# Sidebar
st.sidebar.title("App Information")
st.sidebar.info("This model uses a Random Forest Classifier to estimate risk based on clinical markers.")

# Main Title
st.title("🏥 Diabetes Risk Predictor")
st.write("Adjust the sliders below to see how clinical factors impact the risk score.")

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    glucose = st.slider("Glucose Level", 0, 200, 120)
    bmi = st.slider("BMI", 0.0, 60.0, 25.0)
    age = st.slider("Age", 1, 100, 30)

with col2:
    bp = st.slider("Blood Pressure", 0, 140, 70)
    preg = st.slider("Pregnancies", 0, 20, 0)
    # Add other inputs here if your model needs them!

if st.button("Analyze Risk", use_container_width=True):
    # Prepare the input exactly as the model expects
    features = pd.DataFrame([[preg, glucose, bp, 0, 0, bmi, 0.5, age]], 
                        columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DPF', 'Age'])
    
    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1] * 100

    if prediction == 1:
        st.error(f"High Risk Detected: {prob:.1f}% probability.")
    else:
        st.success(f"Low Risk Detected: {100-prob:.1f}% probability.")

st.divider()
st.caption("Note: This tool is for educational purposes only.")