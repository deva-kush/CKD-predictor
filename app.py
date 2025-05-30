import streamlit as st
import joblib
import numpy as np

# Load saved model
model = joblib.load('ckd_model.pkl')

st.title("🧠 CKD Prediction System")
st.write("Enter your parameters below to check your risk for Chronic Kidney Disease.")

# Collect user input
age = st.number_input("Age", min_value=1, max_value=100)
bp = st.number_input("Blood Pressure", min_value=30, max_value=200)
sg = st.selectbox("Specific Gravity", options=[1.005, 1.010, 1.015, 1.020, 1.025])
al = st.slider("Albumin", 0, 5)
su = st.slider("Sugar", 0, 5)
rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
pc = st.selectbox("Pus Cell", ["normal", "abnormal"])
pcc = st.selectbox("Pus Cell Clumps", ["present", "notpresent"])
ba = st.selectbox("Bacteria", ["present", "notpresent"])
bgr = st.number_input("Blood Glucose Random")
bu = st.number_input("Blood Urea")
sc = st.number_input("Serum Creatinine")
sod = st.number_input("Sodium")
pot = st.number_input("Potassium")
hemo = st.number_input("Hemoglobin")
pcv = st.number_input("Packed Cell Volume")
wc = st.number_input("White Blood Cell Count")
rc = st.number_input("Red Blood Cell Count")
htn = st.selectbox("Hypertension", ["yes", "no"])
dm = st.selectbox("Diabetes Mellitus", ["yes", "no"])
cad = st.selectbox("Coronary Artery Disease", ["yes", "no"])
appet = st.selectbox("Appetite", ["good", "poor"])
pe = st.selectbox("Pedal Edema", ["yes", "no"])
ane = st.selectbox("Anemia", ["yes", "no"])

if st.button("Predict CKD"):
    # Encode & preprocess input
    input_data = np.array([
        age, bp, sg, al, su,
        1 if rbc == "normal" else 0,
        1 if pc == "normal" else 0,
        1 if pcc == "present" else 0,
        1 if ba == "present" else 0,
        bgr, bu, sc, sod, pot, hemo,
        pcv, wc, rc,
        1 if htn == "yes" else 0,
        1 if dm == "yes" else 0,
        1 if cad == "yes" else 0,
        1 if appet == "good" else 0,
        1 if pe == "yes" else 0,
        1 if ane == "yes" else 0
    ]).reshape(1, -1)

    # Predict
    prediction = model.predict(input_data)
    result = "CKD Detected 🛑" if prediction[0] == 1 else "No CKD ✅"
    st.success(result)
