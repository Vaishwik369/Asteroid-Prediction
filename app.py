# import streamlit as st
# import joblib
# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# # Load the trained model and scaler
# rf_model = joblib.load('model.pkl')
# scaler = joblib.load('scaler.pkl')

# # Streamlit app title
# st.title('Asteroid Hazard Prediction')

# # Input fields for asteroid features
# absolute_magnitude = st.number_input('Absolute Magnitude', min_value=0.0, step=0.1)
# est_dia_min = st.number_input('Estimated Diameter in KM (min)', min_value=0.0, step=0.01)
# est_dia_max = st.number_input('Estimated Diameter in KM (max)', min_value=0.0, step=0.01)
# relative_velocity = st.number_input('Relative Velocity (km/sec)', min_value=0.0, step=0.1)
# miss_distance_astronomical = st.number_input('Miss Distance (Astronomical Units)', min_value=0.0, step=0.01)
# eccentricity = st.number_input('Eccentricity', min_value=0.0, step=0.01)
# semi_major_axis = st.number_input('Semi Major Axis', min_value=0.0, step=0.01)
# inclination = st.number_input('Inclination', min_value=0.0, step=0.1)

# # Collect input data into a dictionary
# input_data = {
#     'Absolute Magnitude': absolute_magnitude,
#     'Est Dia in KM(min)': est_dia_min,
#     'Est Dia in KM(max)': est_dia_max,
#     'Relative Velocity km per sec': relative_velocity,
#     'Miss Dist.(Astronomical)': miss_distance_astronomical,
#     'Eccentricity': eccentricity,
#     'Semi Major Axis': semi_major_axis,
#     'Inclination': inclination
# }

# # Convert input data to DataFrame
# input_df = pd.DataFrame([input_data])

# # Scale the input data
# scaled_data = scaler.transform(input_df)

# # Predict if the asteroid is hazardous or not
# if st.button('Predict'):
#     prediction = rf_model.predict(scaled_data)
#     if prediction[0]:
#         st.error('Warning: This asteroid is potentially hazardous!')
#     else:
#         st.success('This asteroid is not hazardous.')

import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the trained model and scaler
rf_model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Add background image using CSS
st.markdown(
    """
    <style>
    body {
        background-image: url("galaxy.jpg");
        background-size: cover;  /* Cover the entire page */
        background-repeat: no-repeat;  /* Do not repeat the image */
        background-attachment: fixed;  /* Keep the background fixed during scrolling */
        background-position: center;  /* Center the background image */
    }

    .reportview-container {
        background-color: rgba(255, 255, 255, 0.8);  /* Semi-transparent white background for better visibility */
        padding: 20px;  /* Padding for content */
        border-radius: 10px;  /* Rounded corners */
    }

    h1, h2, h3, h4, h5, h6, p {
        color: #ffffff;  /* Set text color to white for better visibility */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app title
st.title('Asteroid Hazard Prediction')

# Input fields for asteroid features
absolute_magnitude = st.number_input('Absolute Magnitude', min_value=0.0, step=0.1)
est_dia_min = st.number_input('Estimated Diameter in KM (min)', min_value=0.0, step=0.01)
est_dia_max = st.number_input('Estimated Diameter in KM (max)', min_value=0.0, step=0.01)
relative_velocity = st.number_input('Relative Velocity (km/sec)', min_value=0.0, step=0.1)
miss_distance_astronomical = st.number_input('Miss Distance (Astronomical Units)', min_value=0.0, step=0.01)
eccentricity = st.number_input('Eccentricity', min_value=0.0, step=0.01)
semi_major_axis = st.number_input('Semi Major Axis', min_value=0.0, step=0.01)
inclination = st.number_input('Inclination', min_value=0.0, step=0.1)

# Collect input data into a dictionary
input_data = {
    'Absolute Magnitude': absolute_magnitude,
    'Est Dia in KM(min)': est_dia_min,
    'Est Dia in KM(max)': est_dia_max,
    'Relative Velocity km per sec': relative_velocity,
    'Miss Dist.(Astronomical)': miss_distance_astronomical,
    'Eccentricity': eccentricity,
    'Semi Major Axis': semi_major_axis,
    'Inclination': inclination
}

# Convert input data to DataFrame
input_df = pd.DataFrame([input_data])

# Scale the input data
scaled_data = scaler.transform(input_df)

# Predict if the asteroid is hazardous or not
if st.button('Predict'):
    prediction = rf_model.predict(scaled_data)
    if prediction[0]:
        st.error('Warning: This asteroid is potentially hazardous!')
        st.image('ast.png', caption='Hazardous Asteroid', use_column_width=True)
    else:
        st.success('This asteroid is not hazardous.')
        st.image('giphy.gif', caption='Safe Asteroid', use_column_width=True)


# Add text at the bottom of the page
st.markdown("---")  # This adds a horizontal line above the footer text
st.write("Powered by Vaishwik Vishwakarma")
st.write(" 'Turning data into destiny- keeping Earth safe from the unknown - Vaishwik'")
st.write("© 2024 Asteroid Prediction Inc.")
