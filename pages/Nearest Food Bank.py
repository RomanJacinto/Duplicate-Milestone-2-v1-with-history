import pandas as pd
import streamlit as st

# Set page title and favicon.
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
#create columns for welcome message and logo
col1, col2 = st.columns([0.40, 4])
with col1:
    st.image("https://i.ibb.co/vDgcdkz/250x200.png")
with col2:
    st.header("AI-Powered Smart Meal Solutions for Students", divider="rainbow")

# Load the CSV file
df = pd.read_csv("static/FoodBanks.csv")

# Rename the columns
df = df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})

# Create a streamlit application
st.header('Food Bank Locator')

# Ask the user to input a zip code
zip_code = st.text_input('Enter your zip code to find the nearest food banks in your area:')

if zip_code:
    # Filter the DataFrame based on the user's input
    filtered_df = df[df['Zip Code'] == int(zip_code)]

    if filtered_df.empty:
        st.write("No food banks found in your area.")
    else:
        # Plot the latitude and longitude on a map
        st.map(filtered_df)

        # Display the Business Name of the filtered data
        st.write(filtered_df[['Business Name', 'Address', 'Phone Number', 'Email']])
