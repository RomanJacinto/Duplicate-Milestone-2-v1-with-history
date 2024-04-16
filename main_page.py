import os
import openai
import streamlit as st
from openai import OpenAI
import pandas as pd
import requests

st.title("_Budget Bite_")
st.sidebar.markdown("_Budget Bite_")

st.header("Welcome to _Budget Bite!_", divider="rainbow")
st.subheader("Smart Meal Solutions for Students")


# Create buttons
#weekly_budget = st.radio('Select Budget (per week)', ['$50', '$75', '$100'])
weekly_budget = st.number_input('Please enter your weekly budget in dollars:', min_value=0, max_value=200, value=50, step=5)

diet_type = st.radio('Diet Type:', ['Vegan', 'Vegetarian', 'Eggetarian', 'Pescatarian', 'Non-Vegetarian', 'Mediteranian', 'Paleo',])

dietary_preferneces = st.radio('Dietary Preferences:', ['Balanced Nutrition', 'Low-carb', 'Atkins (High Protein)', 'Ketogenic (High Fat)'])

exclusions = st.multiselect('Dietary Exclusions:', ['Dairy', 'Gluten', 'Pork', 'Fish', 'Beef', 'Nuts'], ['Dairy', 'Gluten', 'Pork', 'Fish', 'Beef', 'Nuts'] )
delimiter = ', '

exclusion_string = delimiter.join(exclusions)

#openai.api_key = os.environ["APIKEY"]

client = OpenAI(api_key="APIKEY")
menu = ""

# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": "Step1: Your job is to provide weekly meal plans for a budget of" + 
         str(weekly_budget) +"that are" + diet_type + "and are" + dietary_preferneces + ". Exclude the ingredients mentioned in" + exclusion_string + "and include price for each meal and a rolling total for each day. Use the format: Breakfast: Oatmeal, $1.50, Lunch: Salad, $3.00, Dinner: Pasta, $4.50. Stop when the total exceeds the budget."},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content

def get_ingredients(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": "Step1: Your job is to make a list of every individual ingredient in this text in a numbered list:" + 
         str(menu) + "exclude any duplicates and add up the total price for the entire grocery list."},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content

   
    

prompt = "Provide weekly meal plan"

# create our streamlit app

with st.form("my_form"):
      
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        menu = get_completion(prompt)
        st.write(menu)
        
        # Google Maps 
        st.write("Would you like directions to the nearest food bank to stay under budget?")
        zip_code = st.number_input('Please enter your zip code:', min_value=501, max_value=99950, value=95192, step=None)
        # Function to get directions to the nearest food bank
        def get_directions(zip_code):
            # Make a request to the Google Maps Directions API
            response = requests.get(f"https://maps.googleapis.com/maps/api/directions/json?origin={zip_code}&destination=food+bank&key=AIzaSyDlb7cyGgePykG4hzZm4rHHPVOjMx7Sop0")

            # Parse the JSON response
            data = response.json()

            # Extract the directions from the response
            directions = data["routes"][0]["legs"][0]["steps"]

            # Return the directions
            return directions
        
        # Check if the user wants directions to the nearest food bank
        if st.checkbox("Get Directions to Nearest Food Bank"):
            directions = get_directions(zip_code)
            st.write("Directions:")
            for step in directions:
                st.write(step["html_instructions"])

        # Get the ingredients
        st.subheader("Here's a shopping list for this menu:")
        grocery_list = str(get_ingredients(menu))
        st.write(grocery_list)
        
