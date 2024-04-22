import pandas as pd
import streamlit as st

# Load the CSV data into a pandas DataFrame
df = pd.read_csv(r"C:\Users\Roman\Desktop\FoodBanks.csv")

# Convert Latitude and Longitude to float
df['Latitude'] = df['Latitude'].astype(float)
df['Longitude'] = df['Longitude'].astype(float)

# Ask the user to enter a zip code
zip_code = st.text_input('Enter your zip code to find the nearest food banks in your area:')

# Filter the DataFrame based on the zip code
df_filtered = df[df['Zip Code'] == zip_code]

# Create a map centered on the first location of the filtered data
map_data = pd.DataFrame(df_filtered[['Latitude', 'Longitude']], columns=['lat', 'lon'])
st.map(map_data)

# Display the Business Name of the filtered data
st.write(df_filtered[['Business Name', 'Address', 'Phone Number', 'Email']])
