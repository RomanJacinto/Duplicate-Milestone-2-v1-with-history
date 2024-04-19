import os
import openai
import streamlit as st
from openai import OpenAI
import pandas as pd
import requests

openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()
#client = OpenAI(api_key="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")

st.set_page_config(layout="wide")
st.title("_Budget Bite_")
st.sidebar.markdown("_Budget Bite_")

st.header("Welcome to _Budget Bite!_", divider="rainbow")
st.subheader("AI-Powered Smart Meal Solutions for Students")

# Create buttons
with st.form(key='columns_in_form'):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
       weekly_budget = st.number_input('Please enter your weekly budget in dollars:', min_value=0, max_value=200, value=0, step=5, placeholder="Please enter a number")
    with c2:
       diet_type = st.radio('Diet Type:', ['Vegan', 'Vegetarian', 'Eggetarian', 'Pescatarian', 'Non-Vegetarian', 'Mediteranian', 'Paleo',])
    with c3:    
       dietary_preferneces = st.radio('Dietary Preferences:', ['Balanced Nutrition', 'Low-carb', 'Atkins (High Protein)', 'Ketogenic (High Fat)'])
    with c4:
       exclusions = st.multiselect('Dietary Exclusions:', ['Dairy', 'Gluten', 'Pork', 'Fish', 'Beef', 'Nuts'], ['Dairy', 'Gluten', 'Pork', 'Fish', 'Beef', 'Nuts'] )
    
    submitted = st.form_submit_button(label = "Submit")
    if submitted:
        delimiter = ', '
        exclusion_string = delimiter.join(exclusions)
        # create a wrapper function
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                    model=model,
                    messages=[
                    {"role":"system",
                    "content": "Step1: Your job is to provide one day meal plan for a budget of" + 
                    str(weekly_budget) +"that are" + diet_type + "and are" + dietary_preferneces + ". exclude these ingredients mentioned in" + exclusion_string + ". Generate only one recipe for each meal. Return a python dictionary with breakfast, lunch, and dinner as a list that gives first the breakfast, then lunch, then dinner recipe. Each recipe should be a string."},
                    {"role": "user",
                    "content": prompt},
                    ]
                )
            return completion.choices[0].message.content
        
        prompt = "Provide a one day meal plan"
        recipes = get_completion(prompt)
        st.write(recipes)

        breakfast = recipes[0]
        lunch = recipes[1]
        dinner = recipes[2]

        st.write("Here's a one day meal plan for you:")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Breakfast")
            # breakfast image generation function
            response = client.images.generate(
                model="dall-e-2",
                prompt="You are a marvelous chef! Your job is create an image for the following recipe " +breakfast[0],
                size="512x512",
                quality="standard",
                n=1,
                )

            image_url = response.data[0].url
            st.image(image_url, caption=breakfast, use_column_width=True)

            def get_breakfast(prompt):
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role":"system",
                    "content": "You are a marvelous chef! Your job is to provide recipe the for" + breakfast[0] + "The recipe should list all ingredients and steps to prepare the dish. Also include the price for the meal."},
                    {"role": "user",
                    "content": prompt},
                    ]
                )
                return completion.choices[0].message.content

            prompt = get_breakfast("get breakfast recipe with ingredients and budget")
            st.write(get_breakfast(prompt))
"""
        with col2:
            st.subheader("Lunch")

            # lunch image generation function
            response = client.images.generate(
                model="dall-e-2",
                prompt="a white siamese cat",
                size="1024x1024",
                quality="standard",
                n=1,
                formats=["jpg"])
            
            image_url = response.data[0].url
            st.image(image_url, caption="White Siamese Cat", use_column_width=True)

            # get lunch recipe
            def get_lunch(prompt):
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role":"system",
                    "content": "Step3: Your job is to provide a lunch meal plan for a budget of" + 
                    str(weekly_budget) +"that are" + diet_type + "and are" + dietary_preferneces + ". Exclude the ingredients mentioned in" + exclusion_string + "and include price for each meal and a rolling total for each day. Use the format: Lunch: Salad, $3.00. Stop when the total exceeds the budget."},
                    {"role": "user",
                    "content": prompt},
                    ]
                )
                return completion.choices[0].message.content
            prompt = get_lunch("get lunch recipe with ingredients and budget")
            st.write(get_lunch(prompt))

        with col3:
            st.subheader("Dinner")

            # dinner image generation function
            response = client.images.generate(
                model="dall-e-2",
                prompt="a white siamese cat",
                size="1024x1024",
                quality="standard",
                n=1,
                formats=["jpg"])
            
            image_url = response.data[0].url
            st.image(image_url, caption="White Siamese Cat", use_column_width=True)

            # get dinner recipe
            def get_dinner(prompt):
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role":"system",
                    "content": "Step4: Your job is to provide a dinner meal plan for a budget of" + 
                    str(weekly_budget) +"that are" + diet_type + "and are" + dietary_preferneces + ". Exclude the ingredients mentioned in" + exclusion_string + "and include price for each meal and a rolling total for each day. Use the format: Dinner: Pasta, $4.50. Stop when the total exceeds the budget."},
                    {"role": "user",
                    "content": prompt},
                    ]
                )
                return completion.choices[0].message.content
            prompt = get_dinner("get dinner recipe with ingredients and budget")

            st.write(get_dinner(prompt))



#openai.api_key = os.environ["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"]


#menu = ""

col1, col2, col3, col4 = st.columns(4)

with col1:
    button1 = st.button('Grocery List')

with col2:
    button2 = st.button('Nearest Food Bank')

with col3:
    button3 = st.button('Nutritional Information')

with col4:
    button4 = st.button('Recipes')

#openai.api_key = os.environ["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"]

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


#menu = ""



#def get_ingredients(prompt, model="gpt-3.5-turbo"):
   #completion = client.chat.completions.create(
        #model=model,
        #messages=[
        #{"role":"system",
         #"content": "Step1: Your job is to make a list of every individual ingredient in this text in a numbered list:" + 
        # str(menu) + "exclude any duplicates and add up the total price for the entire grocery list."},
        #{"role": "user",
        # "content": prompt},
       # ]
    #)
   #return completion.choices[0].message.content

   
    



# create our streamlit app

#with st.form("my_form"):
      
    #submitted = st.form_submit_button(label = "Submit")
    
    #if submitted:
        #menu = get_completion(prompt)
        #st.write(menu)
        
        # Google Maps 
        #st.write("Would you like directions to the nearest food bank to stay under budget?")
        #zip_code = st.number_input('Please enter your zip code:', min_value=501, max_value=99950, value=95192, step=None)
        # Function to get directions to the nearest food bank
        #def get_directions(zip_code):
            # Make a request to the Google Maps Directions API
            #response = requests.get(f"https://maps.googleapis.com/maps/api/directions/json?origin={zip_code}&destination=food+bank&key=AIzaSyDlb7cyGgePykG4hzZm4rHHPVOjMx7Sop0")

            # Parse the JSON response
            #data = response.json()

            # Extract the directions from the response
            #directions = data["routes"][0]["legs"][0]["steps"]

            # Return the directions
            #return directions
        
        # Check if the user wants directions to the nearest food bank
        #if st.checkbox("Get Directions to Nearest Food Bank"):
            #directions = get_directions(zip_code)
            #st.write("Directions:")
            #for step in directions:
                #st.write(step["html_instructions"])

        # Get the ingredients
        #st.subheader("Here's a shopping list for this menu:")
        #grocery_list = str(get_ingredients(menu))
        #st.write(grocery_list)
        
"""