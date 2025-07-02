import streamlit as st
import requests

st.title("🩺 Smart Health Risk Predictor")

# Input form
age = st.slider("Age", 10, 100)
bp = st.number_input("Blood Pressure", min_value=50, max_value=200)
sugar = st.number_input("Sugar Level", min_value=70, max_value=300)
chol = st.number_input("Cholesterol", min_value=100, max_value=400)

if st.button("Predict Health Risk"):
    input_data = {
        "age": age,
        "bp": bp,
        "sugar": sugar,
        "chol": chol
    }
    response = requests.post("http://localhost:5000/predict", json=input_data)
    result = response.json()
    st.success(f"Prediction: {'⚠️ At Risk' if result['risk'] == 1 else '✅ Healthy'}")
