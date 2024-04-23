import pandas as pd
import streamlit as st

# Load the CSV file
df = pd.read_csv(r"C:\Users\Roman\Desktop\FoodBanks.csv")

# Rename the columns
df = df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})

# Create a streamlit application
st.title('Food Bank Locator')

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
