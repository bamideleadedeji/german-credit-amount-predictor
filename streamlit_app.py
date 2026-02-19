import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the saved model and scaler
model = joblib.load('credit_model.pkl')
scaler = joblib.load('scaler.pkl')

st.set_page_config(page_title="Credit Predictor", layout="wide")

st.title("Credit Amount Prediction Portal")
st.info("Deploying from branch: **master**")

# Sidebar for inputs
st.sidebar.header("Customer Details")

def get_input():
    # Numeric
    age = st.sidebar.number_input("Age", 18, 100, 30)
    job = st.sidebar.slider("Job Level", 0, 3, 2)
    duration = st.sidebar.number_input("Duration (Months)", 1, 72, 12)
    
    # Categorical logic
    sex = st.sidebar.radio("Sex", ["male", "female"])
    housing = st.sidebar.selectbox("Housing", ["own", "rent", "free"])
    savings = st.sidebar.selectbox("Savings", ["moderate", "quite rich", "rich", "none", "little"])
    checking = st.sidebar.selectbox("Checking Account", ["moderate", "rich", "none", "little"])
    purpose = st.sidebar.selectbox("Purpose", ["car", "domestic appliances", "education", "furniture/equipment", "radio/TV", "repairs", "vacation/others"])

    # This dictionary follows your specific column list ORDER
    data = {
        'Age': age,
        'Job': job,
        'Duration': duration,
        'Sex_male': 1 if sex == 'male' else 0,
        'Housing_own': 1 if housing == 'own' else 0,
        'Housing_rent': 1 if housing == 'rent' else 0,
        'Saving accounts_moderate': 1 if savings == 'moderate' else 0,
        'Saving accounts_none': 1 if savings == 'none' else 0,
        'Saving accounts_quite rich': 1 if savings == 'quite rich' else 0,
        'Saving accounts_rich': 1 if savings == 'rich' else 0,
        'Checking account_moderate': 1 if checking == 'moderate' else 0,
        'Checking account_none': 1 if checking == 'none' else 0,
        'Checking account_rich': 1 if checking == 'rich' else 0,
        'Purpose_car': 1 if purpose == 'car' else 0,
        'Purpose_domestic appliances': 1 if purpose == 'domestic appliances' else 0,
        'Purpose_education': 1 if purpose == 'education' else 0,
        'Purpose_furniture/equipment': 1 if purpose == 'furniture/equipment' else 0,
        'Purpose_radio/TV': 1 if purpose == 'radio/TV' else 0,
        'Purpose_repairs': 1 if purpose == 'repairs' else 0,
        'Purpose_vacation/others': 1 if purpose == 'vacation/others' else 0,
    }
    return pd.DataFrame(data, index=[0])

df_input = get_input()

# Displaying the input
st.subheader("Current Input Data")
st.table(df_input)

if st.button("Predict Recommended Amount"):
    # Scale and Predict
    scaled_data = scaler.transform(df_input)
    prediction = model.predict(scaled_data)
    
    st.success(f"### Predicted Credit Amount: {prediction[0]:,.2f} DM")
