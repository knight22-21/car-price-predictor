import streamlit as st
import pickle
import pandas as pd

# Load the pipeline
pipeline = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

# Load cleaned car data for dropdown options
car = pd.read_csv('Cleaned_data.csv')

# Title of the app
st.title("Car Price Prediction")

# Create dropdowns for user input
companies = sorted(car['company'].unique())
car_models = sorted(car['name'].unique())
years = sorted(car['year'].unique(), reverse=True)
fuel_types = car['fuel_type'].unique()

selected_company = st.selectbox('Select Company', companies)
selected_model = st.selectbox('Select Car Model', car_models)
selected_year = st.selectbox('Select Year', years)
selected_fuel_type = st.selectbox('Select Fuel Type', fuel_types)
driven_kms = st.number_input('Enter KMs Driven', min_value=0.0, step=100.0)

# Button to trigger prediction
if st.button('Predict Price'):
    try:
        input_data = pd.DataFrame({
            'name': [selected_model],
            'company': [selected_company],
            'year': [selected_year],
            'kms_driven': [driven_kms],
            'fuel_type': [selected_fuel_type]
        })

        # Make prediction using the pipeline
        prediction = pipeline.predict(input_data)

        # Display the result
        st.success(f'Predicted Price: ₹{round(prediction[0], 2)}')

    except Exception as e:
        st.error(f'Error: {str(e)}')

