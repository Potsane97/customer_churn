import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('churn_model.pkl')

st.title("Customer Churn Prediction App")
st.write("Enter customer details to predict churn.")

# Numeric Inputs
tenure = st.number_input("Tenure (months)", min_value=0, max_value=1000, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=1000.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=50000.0, value=2000.0)

# Categorical Inputs
contract_type = st.selectbox(
    "Contract Type",
    options={0: "Month-to-month", 1: "One year", 2: "Two year"},
    index=0
)
internet_service = st.selectbox(
    "Internet Service",
    options={0: "No", 1: "DSL", 2: "Fiber optic"},
    index=1
)

# Map categorical selections to model input integers
contract_type_val = list(contract_type.keys())[list(contract_type.values()).index(contract_type)] if isinstance(contract_type, dict) else contract_type
internet_service_val = list(internet_service.keys())[list(internet_service.values()).index(internet_service)] if isinstance(internet_service, dict) else internet_service

# Since selectbox returns keys, we need to get the selected integer key:
contract_type_val = contract_type if isinstance(contract_type, int) else 0
internet_service_val = internet_service if isinstance(internet_service, int) else 0

# Prepare feature vector (ensure order matches model training)
input_features = np.array([[
    tenure,
    monthly_charges,
    total_charges,
    contract_type_val,
    internet_service_val
]])

if st.button("Predict"):
    prediction = model.predict(input_features)[0]
    result = "Churn" if prediction == 1 else "Not Churn"
    st.success(f"Prediction: {result}")
