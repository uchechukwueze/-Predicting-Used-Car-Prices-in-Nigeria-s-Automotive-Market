import streamlit as st
import pandas as pd
import joblib
import numpy as np


# Load saved objects
scaler = joblib.load('full_pipeline.pkl')
encode_Year_of_manufacture = joblib.load('encode_year_of_manufacture.pkl')
encode_Condition = joblib.load('encode_condition.pkl')
encode_Mileage = joblib.load('encode_mileage.pkl')
encode_Engine_Size = joblib.load('encode_engine_size.pkl')
encode_Fuel = joblib.load('encode_fuel.pkl')
encode_Transmission = joblib.load('encode_transmission.pkl')
encode_Build = joblib.load('encode_build.pkl')
encode_State = joblib.load('encode_state.pkl')

model = joblib.load('best_model.pkl')

st.set_page_config(
    page_title="Nigeria Used Car Predictor",
    page_icon=":Automative:",
    layout="centered"
)

st.title("Nigeria Use Car Predictor")
st.write("Enter the details below to predict the Car Price.")

with st.form("car_form"):
    col1, col2 = st.columns(2)

    with col1:
        Year_of_manufacture = st.number_input("Year of car manufacture")
        Condition = st.selectbox('Condition',("Nigerian Used","Foreign Used"))
        Mileage = st.number_input("Mileage")
        Engine_Size = st.number_input("Engine Size")
    
    with col2:
        Fuel = st.selectbox('Fuel',("Petrol","Hybrid","Diesel"))
        Transmission = st.selectbox('Transmission',("Manual","Automatic","CVT","AMT"))
        Build = st.selectbox('Build',("SUV","other"))
        State = st.selectbox("State", options=encode_State.classes_)
    
    result =""
    
    submitted = st.form_submit_button("Predict Price")

    if submitted:
        # Create input dataframe
        input_data = pd.DataFrame({
            'Year_of_manufacture': [Year_of_manufacture],
            'Condition': [Condition],
            'Mileage': [Mileage],
            'Engine_Size': [Engine_Size],
            'Fuel': [Fuel],
            'Transmission': [Transmission],
            'Build': [Build],
            'State': [State],
            
        })

# ['Make', 'Condition', 'Fuel', 'Transmission', 'Build', 'State'

        # Encode categorical features
        # input_data['Condition'] = encode_Condition.transform(input_data['Condition'])
        # input_data['Fuel'] = encode_Fuel.transform(input_data['Fuel'])
        # input_data['Transmission'] = encode_Transmission.transform(input_data['Transmission'])
        # input_data['Build'] = encode_Fuel.transform(input_data['Build'])
        # input_data['State'] = encode_State.transform(input_data['State'])
        
        
        input_data['Condition'] = encode_Condition.transform(input_data['Condition'])
        input_data['Fuel'] = encode_Fuel.transform(input_data['Fuel'])
        input_data['Transmission'] = encode_Transmission.transform(input_data['Transmission'])
        input_data['Build'] = encode_Build.transform(input_data['Build'])
        input_data['State'] = encode_State.transform(input_data['State'])
        
        # Scale numeric features
        # numeric_features = ['Year_of_manufacture', 'Mileage', 'Engine_Size']
        # input_data[numeric_features] = scaler.transform(input_data[numeric_features])
        
        numeric_features = ['Year_of_manufacture', 'Mileage', 'Engine_size']
        input_data[numeric_features] = scaler.transform(input_data[numeric_features])
     
        # Predict
        prediction = model.predict(input_data)[0]
        
        st.success(f"**The predicted car price is**: NGN ₦{prediction:,.2f}")
        st.info("ℹ️ This is an estimated cost based on the information you provided.")

        # st.success(f"**The predicted health insurance cost is**: ${prediction:.2f}")