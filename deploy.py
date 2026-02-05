import streamlit as st 
import joblib
import numpy as np

st.title("Diabetes Predictor")
st.write("Enter patient details to predict the likelihood of diabetes:")

pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose", min_value=0, max_value=200, value=120)
bloodpressure = st.number_input("BloodPressure", min_value=0, max_value=150, value=70)
skinthickness = st.number_input("SkinThickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=79)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
age = st.number_input("Age", min_value=1, max_value=120, value=30)

model=joblib.load("model.joblib")

if(st.button("Predict")):
  features = np.array([[pregnancies, glucose, bloodpressure, skinthickness,insulin, bmi, dpf, age]])
  prediction = model.predict(features)
  
  if prediction[0] == 1:
    st.write("This patient is likely to have diabetes.")
  else:
    st.write("This patient is unlikely to have diabetes.")