# import streamlit as st
# import pandas as pd
# import joblib

# # --------------------------------------------------
# # Load trained pipeline (includes encoders + scaler + model)
# # --------------------------------------------------
# pipeline = joblib.load("full_pipeline.pkl")

# # --------------------------------------------------
# # Streamlit page config
# # --------------------------------------------------
# st.set_page_config(
#     page_title="Nigeria Used Car Price Predictor",
#     page_icon="🚗",
#     layout="centered"
# )

# st.title("🚗 Nigeria Used Car Price Predictor")
# st.write("Enter the car details below to predict the estimated price.")

# # --------------------------------------------------
# # Input Form
# # --------------------------------------------------
# with st.form("car_form"):
#     col1, col2 = st.columns(2)

#     with col1:
#         Year_of_manufacture = st.number_input(
#             "Year of Manufacture", min_value=1990, max_value=2026, step=1
#         )
#         Condition = st.selectbox(
#             "Condition", ["Nigerian Used", "Foreign Used"]
#         )
#         Mileage = st.number_input(
#             "Mileage (km)", min_value=0, step=1000
#         )
#         Engine_size = st.number_input(
#             "Engine Size (L)", min_value=0.5, step=0.1
#         )

#     with col2:
#         Fuel = st.selectbox(
#             "Fuel Type", ["Petrol", "Diesel", "Hybrid"]
#         )
#         Transmission = st.selectbox(
#             "Transmission", ["Automatic", "Manual", "CVT", "AMT"]
#         )
#         Build = st.selectbox(
#             "Build", ["SUV", "Sedan", "Hatchback", "Other"]
#         )
#         State = st.text_input(
#             "State (e.g. Lagos, Abuja)"
#         )

#     submitted = st.form_submit_button("Predict Price")

# # --------------------------------------------------
# # Prediction
# # --------------------------------------------------
# if submitted:
#     # Create input DataFrame (MUST match training column names)
#     input_data = pd.DataFrame({
#         "Year_of_manufacture": [Year_of_manufacture],
#         "Mileage": [Mileage],
#         "Engine_size": [Engine_size],
#         "Condition": [Condition],
#         "Fuel": [Fuel],
#         "Transmission": [Transmission],
#         "Build": [Build],
#         "State": [State]
#     })

#     try:
#         prediction = pipeline.predict(input_data)[0]

#         st.success(f"💰 Estimated Car Price: NGN ₦{prediction:,.2f}")
#         st.info("This is an estimate based on the information provided.")

#     except Exception as e:
#         st.error("⚠️ An error occurred during prediction.")
#         st.exception(e)


import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Load trained pipeline (includes encoders + scaler + model)
# --------------------------------------------------
pipeline = joblib.load("full_pipeline.pkl")

# --------------------------------------------------
# Streamlit page config
# --------------------------------------------------
st.set_page_config(
    page_title="Nigeria Used Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Nigeria Used Car Price Predictor")
st.write("Enter the car details below to predict the estimated price.")

# --------------------------------------------------
# Input Form
# --------------------------------------------------
with st.form("car_form"):
    col1, col2 = st.columns(2)

    with col1:
        Year_of_manufacture = st.number_input(
            "Year of Manufacture", min_value=1990, max_value=2026, step=1
        )
        Condition = st.selectbox(
            "Condition", ["Nigerian Used", "Foreign Used"]
        )
        Mileage = st.number_input(
            "Mileage (km)", min_value=0, step=1000
        )
        Engine_size = st.number_input(
            "Engine Size (L)", min_value=0.5, step=0.1
        )

    with col2:
        Fuel = st.selectbox(
            "Fuel Type", ["Petrol", "Diesel", "Hybrid"]
        )
        Transmission = st.selectbox(
            "Transmission", ["Automatic", "Manual", "CVT", "AMT"]
        )
        Build = st.selectbox(
            "Build", ["SUV", "Sedan", "Hatchback", "Other"]
        )
        State = st.text_input(
            "State (e.g. Lagos, Abuja)"
        )

    submitted = st.form_submit_button("Predict Price")

# --------------------------------------------------
# Prediction
# --------------------------------------------------
if submitted:
    # Corrected column names to match pipeline
    input_data = pd.DataFrame({
        "Year of manufacture": [Year_of_manufacture],
        "Mileage": [Mileage],
        "Engine_Size": [Engine_size],
        "Condition": [Condition],
        "Fuel": [Fuel],
        "Transmission": [Transmission],
        "Build": [Build],
        "State": [State]
    })

    # Optional: ensure all expected columns exist
    expected_columns = pipeline.feature_names_in_ if hasattr(pipeline, 'feature_names_in_') else input_data.columns
    for col in expected_columns:
        if col not in input_data.columns:
            input_data[col] = 0  # fill missing columns

    try:
        prediction = pipeline.predict(input_data)[0]

        st.success(f"💰 Estimated Car Price: NGN ₦{prediction:,.2f}")
        st.info("This is an estimate based on the information provided.")

    except Exception as e:
        st.error("⚠️ An error occurred during prediction.")
        st.exception(e)
