import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("/home/deva_kush/ml_projects/CKD/notebooks/ckd_model.pkl")

# Styling
st.set_page_config(page_title="CKD Risk Checker", layout="wide")
st.markdown("<h1 style='text-align: center;'>🩺 CKD Risk Checker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>An intelligent tool to help you understand your risk of Chronic Kidney Disease. Just enter a few health parameters to get started.</p>", unsafe_allow_html=True)

st.markdown("---")

# Input Layout
st.header("📋 Enter Your Medical Details")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age (years)", min_value=1, max_value=100, help="Your current age in years.")
    sg = st.selectbox("Specific Gravity", [1.005, 1.010, 1.015, 1.020, 1.025], help="Helps evaluate kidney function.")
    rbc = st.selectbox("Red Blood Cells", ["Normal", "Abnormal"])
    pcc = st.selectbox("Pus Cell Clumps", ["Present", "Not Present"])
    bu = st.number_input("Blood Urea (mg/dL)", help="High levels may indicate kidney dysfunction.")
    pot = st.number_input("Potassium (mEq/L)", help="Abnormal levels can affect kidney and heart function.")
    pcv = st.number_input("Packed Cell Volume (%)")
    htn = st.selectbox("Hypertension", ["Yes", "No"])
    appet = st.selectbox("Appetite", ["Good", "Poor"])

with col2:
    bp = st.number_input("Blood Pressure (mm Hg)", min_value=30, max_value=200)
    al = st.slider("Albumin", 0, 5, help="Protein in urine, higher levels can signal kidney damage.")
    pc = st.selectbox("Pus Cells", ["Normal", "Abnormal"])
    ba = st.selectbox("Bacteria", ["Present", "Not Present"])
    sc = st.number_input("Serum Creatinine (mg/dL)")
    hemo = st.number_input("Hemoglobin (g/dL)")
    wc = st.number_input("WBC Count (cells/cumm)")
    dm = st.selectbox("Diabetes", ["Yes", "No"])
    pe = st.selectbox("Pedal Edema", ["Yes", "No"])

with col3:
    su = st.slider("Sugar", 0, 5)
    bgr = st.number_input("Blood Glucose Random (mg/dL)")
    sod = st.number_input("Sodium (mEq/L)")
    rc = st.number_input("RBC Count (millions/cumm)")
    cad = st.selectbox("Coronary Artery Disease", ["Yes", "No"])
    ane = st.selectbox("Anemia", ["Yes", "No"])

# Prediction Logic
if st.button("🧠 Predict My CKD Risk"):

    input_data = np.array([
        age, bp, sg, al, su,
        1 if rbc.lower() == "normal" else 0,
        1 if pc.lower() == "normal" else 0,
        1 if pcc.lower() == "present" else 0,
        1 if ba.lower() == "present" else 0,
        bgr, bu, sc, sod, pot, hemo,
        pcv, wc, rc,
        1 if htn.lower() == "yes" else 0,
        1 if dm.lower() == "yes" else 0,
        1 if cad.lower() == "yes" else 0,
        1 if appet.lower() == "good" else 0,
        1 if pe.lower() == "yes" else 0,
        1 if ane.lower() == "yes" else 0
    ]).reshape(1, -1)

    prediction = model.predict(input_data)[0]

    st.markdown("---")
    st.subheader("🧾 Prediction Result")

    if prediction == 1:
        st.markdown(
            """
            <div style="background-color:#ff4d4d;padding:20px;border-radius:10px;text-align:center;color:white;font-size:20px;">
            ⚠️ <strong>High Risk Detected:</strong><br>
            Our model predicts that you may have a risk of Chronic Kidney Disease.<br>
            Please consult a healthcare professional immediately.
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div style="background-color:#28a745;padding:20px;border-radius:10px;text-align:center;color:white;font-size:20px;">
            ✅ <strong>No CKD Risk Detected:</strong><br>
            You're currently not at risk of Chronic Kidney Disease.<br>
            Maintain regular checkups and a healthy lifestyle.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.info("⚠️ This tool provides a preliminary risk assessment. It is not a substitute for professional medical advice.")
