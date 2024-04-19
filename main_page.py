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
       weekly_budget = st.number_input('Please enter your daily budget in dollars:', min_value=0, max_value=200, value=None, step=5, placeholder="Please enter a number")
    with c2:
       diet_type = st.radio('Diet Type:', ['Vegan', 'Vegetarian', 'Pescatarian', 'Non-Vegetarian', 'Mediteranian', 'Paleo',])
    with c3:    
       dietary_preferneces = st.radio('Dietary Preferences:', ['Balanced Nutrition', 'Low-carb', 'Atkins (High Protein)', 'Ketogenic (High Fat)'])
    with c4:
       exclusions = st.multiselect('Dietary Exclusions:', ['Dairy', 'Gluten', 'Pork', 'Fish', 'Beef', 'Nuts'], ['Dairy', 'Gluten'] )
    
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
                    str(weekly_budget) +"that are" + diet_type + "and are" + dietary_preferneces + ". exclude these ingredients mentioned in" + exclusion_string + ". Generate only one recipe for each meal and the output should just be the name of the recipe, do not include any ingredients or instructions. Return a comma separated strings that gives first the breakfast, then lunch, then dinner recipe"},
                    {"role": "user",
                    "content": prompt},
                    ]
                )
            return completion.choices[0].message.content
        
        prompt = "Provide a one day meal plan"
        recipes = get_completion(prompt)
        recipes_list = recipes.split(",")
        #st.write(recipes_list)

        breakfast = recipes_list[0]
        #st.write(breakfast)
        lunch = recipes_list[1]
        #st.write(lunch)
        dinner = recipes_list[2]
        #st.write(dinner)

        st.write("Here's a one day meal plan for you:")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Breakfast")
            # breakfast image generation function
            response = client.images.generate(
                model="dall-e-2",
                prompt= breakfast,
                size="512x512",
                quality="standard",
                n=1,
                )

            image_url = response.data[0].url
            st.image(image_url, caption=breakfast, use_column_width=True)

            #get breakfast recipe
            def get_breakfast(prompt):
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role":"system",
                    "content": "You are a chef and your job is to provide a recipe asked by the prompt. The recipe should list all ingredients and steps to prepare only one serving of the dish. Use the format: Name of the recipe, a list of ingredients, and step by step instructions."},
                    {"role": "user",
                    "content": prompt},
                    ]
                )
                return completion.choices[0].message.content

            prompt = get_breakfast(breakfast)
            st.write(get_breakfast(prompt))

            # get nutritional information
            def get_nutrition(prompt):
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role":"system",
                    "content": "You are a nutritionist and your job is to provide the nutritional information for the recipe asked by the prompt. The information should include the both macro and micro nutrients. Use the USDA database for the nutritional information. The format of the output should be in a table with the following columns: Nutrient, Amount per serving, Daily Value. The daily value should be calculated based on a 2000 calorie diet."},
                    {"role": "user",
                    "content": prompt},
                    ]
                )
                return completion.choices[0].message.content
            
            prompt = get_nutrition(breakfast)
            st.write(get_nutrition(prompt))

            
        with col2:
            st.subheader("Lunch")

            # lunch image generation function
            response = client.images.generate(
                model="dall-e-2",
                prompt= lunch,
                size="512x512",
                quality="standard",
                n=1,
                )
            
            image_url = response.data[0].url
            st.image(image_url, caption=lunch, use_column_width=True)

            # get lunch recipe
            def get_lunch(prompt):
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role":"system",
                    "content": "You are a chef and your job is to provide a recipe asked by the prompt. The recipe should list all ingredients and steps to prepare only one serving of the dish. Use the format: Name of the recipe, a list of ingredients, and step by step instructions."},
                    {"role": "user",
                    "content": prompt},
                    ]
                )
                return completion.choices[0].message.content
            prompt = get_lunch(lunch)
            st.write(get_lunch(prompt))

            # get nutritional information
            def get_nutrition(prompt):
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role":"system",
                    "content": "You are a nutritionist and your job is to provide the nutritional information for the recipe asked by the prompt. The information should include the both macro and micro nutrients. Use the USDA database for the nutritional information. The format of the output should be in a table with the following columns: Nutrient, Amount per serving, Daily Value. The daily value should be calculated based on a 2000 calorie diet."},
                    {"role": "user",
                    "content": prompt},
                    ]
                )
                return completion.choices[0].message.content
            
            prompt = get_nutrition(lunch)
            st.write(get_nutrition(prompt))

        with col3:
            st.subheader("Dinner")

            # dinner image generation function
            response = client.images.generate(
                model="dall-e-2",
                prompt=dinner,
                size="512x512",
                quality="standard",
                n=1,
                )
            
            image_url = response.data[0].url
            st.image(image_url, caption=dinner, use_column_width=True)

            # get dinner recipe
            def get_dinner(prompt):
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role":"system",
                    "content": "You are a chef and your job is to provide a recipe asked by the prompt. The recipe should list all ingredients and steps to prepare only one serving the dish. Use the format: Name of the recipe, a list of ingredients, and step by step instructions."},
                    {"role": "user",
                    "content": prompt},
                    ]
                )
                return completion.choices[0].message.content
            
            prompt = get_dinner(dinner)
            st.write(get_dinner(prompt))

            # get nutritional information
            def get_nutrition(prompt):
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role":"system",
                    "content": "You are a nutritionist and your job is to provide the nutritional information for the recipe asked by the prompt. The information should include the both macro and micro nutrients. Use the USDA database for the nutritional information. The format of the output should be in a table with the following columns: Nutrient, Amount per serving, Daily Value. The daily value should be calculated based on a 2000 calorie diet."},
                    {"role": "user",
                    "content": prompt},
                    ]
                )
                return completion.choices[0].message.content
            
            prompt = get_nutrition(dinner)
            st.write(get_nutrition(prompt))

        st.subheader("Would you like a three day or seven day meal plan?")

        coln1, coln2 = st.columns(2)
        with coln1:
            submitted_three_day = st.checkbox(label = "Yes, I would like a three day meal plan")
            
            if submitted_three_day:
                st.write("Here's a three day meal plan for you:")
                three_day_budget = weekly_budget * 3
                # create a wrapper function
                def get_completion(prompt, model="gpt-3.5-turbo"):
                    completion = client.chat.completions.create(
                            model=model,
                            messages=[
                            {"role":"system",
                            "content": "Step1: Your job is to provide a three day meal plan for a budget of" + 
                            str(three_day_budget) +"that are" + diet_type + "and are" + dietary_preferneces + ". Exclude the ingredients mentioned in" + exclusion_string + "and include price for each meal. Use the format: Breakfast: Oatmeal, $1.50, Lunch: Salad, $3.00, Dinner: Pasta, $4.50. Stop when the total exceeds the budget and tell the user to reach out to the nearest food bank to stay under budget."},
                            {"role": "user",
                            "content": prompt},
                            ]
                        )
                    return completion.choices[0].message.content
                prompt = "provide a three day meal plan"
                three_day_recipes = get_completion(prompt)
                st.write(three_day_recipes)
        
        with coln2:
            submitted_seven_day = st.checkbox(label = "Yes, I would like a seven day meal plan")
            
            if submitted_seven_day:
                st.write("Here's a seven day meal plan for you:")
                seven_day_budget = weekly_budget * 7
                # create a wrapper function
                def get_completion(prompt, model="gpt-3.5-turbo"):
                    completion = client.chat.completions.create(
                            model=model,
                            messages=[
                            {"role":"system",
                            "content": "Step1: Your job is to provide a seven day meal plan for a budget of" + 
                            str(seven_day_budget) +"that are" + diet_type + "and are" + dietary_preferneces + ". Exclude the ingredients mentioned in" + exclusion_string + "and include price for each meal. Use the format: Breakfast: Oatmeal, $1.50, Lunch: Salad, $3.00, Dinner: Pasta, $4.50. Stop when the total exceeds the budget and tell the user to reach out to the nearest food bank to stay under budget."},
                            {"role": "user",
                            "content": prompt},
                            ]
                        )
                    return completion.choices[0].message.content
                prompt = "provide a five day meal plan"
                five_day_recipes = get_completion(prompt)
                st.write(five_day_recipes)


#openai.api_key = os.environ["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"]

#menu = ""


#openai.api_key = os.environ["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"]

#def get_completion(prompt, model="gpt-3.5-turbo"):
            #completion = client.chat.completions.create(
                    #model=model,
                    #messages=[
                    #{"role":"system",
                    #"content": "Step1: Your job is to provide weekly meal plans for a budget of" + 
                    #str(weekly_budget) +"that are" + diet_type + "and are" + dietary_preferneces + ". Exclude the ingredients mentioned in" + exclusion_string + "and include price for each meal and a rolling total for each day. Use the format: Breakfast: Oatmeal, $1.50, Lunch: Salad, $3.00, Dinner: Pasta, $4.50. Stop when the total exceeds the budget."},
                    #{"role": "user",
                    #"content": prompt},
                    #]
                #)
            #return completion.choices[0].message.content


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
        
