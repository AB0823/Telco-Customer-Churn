import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")
st.title("📊 Customer Churn Prediction Dashboard")

st.markdown("Predict whether a customer is likely to churn based on their profile.")
st.sidebar.header("Customer Details")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
Partner = st.sidebar.selectbox("Has Partner?", ["Yes", "No"])
Dependents = st.sidebar.selectbox("Has Dependents?", ["Yes", "No"])
tenure = st.sidebar.slider("Tenure (months)", 0, 72)
PhoneService = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.sidebar.selectbox("Multiple Lines", ["Yes", "No"])
InternetService = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
OnlineSecurity = st.sidebar.selectbox("Online Security", ["Yes", "No"])
OnlineBackup = st.sidebar.selectbox("Online Backup", ["Yes", "No"])
DeviceProtection = st.sidebar.selectbox("Device Protection", ["Yes", "No"])
TechSupport = st.sidebar.selectbox("Tech Support", ["Yes", "No"])
StreamingTV = st.sidebar.selectbox("Streaming TV", ["Yes", "No"])
StreamingMovies = st.sidebar.selectbox("Streaming Movies", ["Yes", "No"])
Contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.sidebar.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)
MonthlyCharges = st.sidebar.number_input("Monthly Charges", min_value=0.0)
TotalCharges = st.sidebar.number_input("Total Charges", min_value=0.0)

input_df = pd.DataFrame({
    'gender': [str(gender)],
    'SeniorCitizen': [int(SeniorCitizen)],
    'Partner': [str(Partner)],
    'Dependents': [str(Dependents)],
    'tenure': [int(tenure)],
    'PhoneService': [str(PhoneService)],
    'MultipleLines': [str(MultipleLines)],
    'InternetService': [str(InternetService)],
    'OnlineSecurity': [str(OnlineSecurity)],
    'OnlineBackup': [str(OnlineBackup)],
    'DeviceProtection': [str(DeviceProtection)],
    'TechSupport': [str(TechSupport)],
    'StreamingTV': [str(StreamingTV)],
    'StreamingMovies': [str(StreamingMovies)],
    'Contract': [str(Contract)],
    'PaperlessBilling': [str(PaperlessBilling)],
    'PaymentMethod': [str(PaymentMethod)],
    'MonthlyCharges': [float(MonthlyCharges)],
    'TotalCharges': [float(TotalCharges)]
})
if st.button("🔍 Predict Churn"):
    with st.spinner("Analyzing customer data..."):
        prob = model.predict_proba(input_df)[0][1]
    st.subheader("📈 Prediction Result")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Churn Probability", f"{prob:.2%}")
    with col2:
        if prob > 0.5:
            st.error("⚠️ High Risk of Churn")
        else:
            st.success("✅ Low Risk of Churn")
    if prob > 0.5:
        st.info("💡 Recommendation: Offer discounts or long-term plans to retain this customer.")
with st.expander("🔎 View Input Data"):
    st.write(input_df)