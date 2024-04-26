import os
import openai
import streamlit as st
from openai import OpenAI
import pandas as pd
import requests
from streamlit_navigation_bar import st_navbar
import navbar

openai.api_key = os.environ["APIKEY"]
client = OpenAI()

#client = OpenAI(api_key='APIKEY')

# Set page title and favicon.
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

pages = ["Home","Budgeted Meal Plans", "Dorm Specials", "Explore Recipes", "Nearest Food Bank", "Learn"]

# Create a navigation bar
page = st_navbar(pages)

functions = {
    "Home": navbar.home,
    "Budgeted Meal Plans": navbar.mealplan,
    "Dorm Specials": navbar.dorm,
    "Explore Recipes": navbar.explore,
    "Nearest Food Bank": navbar.bank,
    "Learn": navbar.learn,
    
}

go_to = functions.get(page)
if go_to:
    go_to()


#create columns for welcome message and logo
col1, col2 = st.columns([0.40, 4])
with col1:
    st.image("https://i.ibb.co/vDgcdkz/250x200.png")
with col2:
    st.header("AI-Powered Smart Meal Solutions for Students", divider="rainbow")

# Create Buttons
c1, c2, c3, c4 = st.columns(4)
with c1:
    weekly_budget = st.number_input('Please enter your daily budget in dollars:', min_value=0, max_value=200, value=0, step=5, placeholder="Please enter a number")
with c2:
    diet_type = st.radio('Diet Type:', ['Vegan', 'Vegetarian', 'Pescatarian', 'Non-Vegetarian', 'Paleo',])
with c3:    
    dietary_preferneces = st.radio('Dietary Preferences:', ['Balanced Nutrition', 'Low-carb', 'Atkins (High Protein)', 'Ketogenic (High Fat)'])
with c4:
    exclusions = st.multiselect('Dietary Exclusions:', ['Dairy', 'Gluten', 'Pork', 'Fish', 'Beef', 'Nuts'], ['Dairy', 'Gluten'] )
delimiter = ', '
exclusion_string = delimiter.join(exclusions)
# One day meal plan
submitted = st.button(label = "One Day Meal Plan")
if submitted:
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
    st.markdown(''':red[**NOTE 1: These recipes are AI-generated and Budget Bite has not verified it for accuracy or safety. It may contain errors. Always use your best judgement when making AI-generated dishes.**]''')
    st.markdown(''':red[**NOTE 2: Please note that the prices of the ingredients mentioned are based on average costs and are intended for general reference only. Actual prices may vary depending on the availability of ingredients and location-specific factors. We encourage readers to check local markets for the most current pricing information.**]''')
        


submitted_three_day = st.button(label= "Three Day Meal Plan")

if submitted_three_day:
    st.write("Here's a three day meal plan for you:")    
    for i in range(1,4,1):
        st.markdown("----", unsafe_allow_html=True)
        st.write("Day", i)
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

    st.markdown(''':red[**NOTE 1: These recipes are AI-generated and Budget Bite has not verified it for accuracy or safety. It may contain errors. Always use your best judgement when making AI-generated dishes.**]''')
    st.markdown(''':red[**NOTE 2: Please note that the prices of the ingredients mentioned are based on average costs and are intended for general reference only. Actual prices may vary depending on the availability of ingredients and location-specific factors. We encourage readers to check local markets for the most current pricing information.**]''')



# Seven day meal plan
submitted_seven_day = st.button(label= "Seven Day Meal Plan")

if submitted_seven_day:
    st.write("Here's a seven day meal plan for you:")
    st.markdown("----", unsafe_allow_html=True)
    for i in range(1,8,1):
        st.write("Day", i)
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
            
            
    st.markdown(''':red[**NOTE 1: These recipes are AI-generated and Budget Bite has not verified it for accuracy or safety. It may contain errors. Always use your best judgement when making AI-generated dishes.**]''')
    st.markdown(''':red[**NOTE 2: Please note that the prices of the ingredients mentioned are based on average costs and are intended for general reference only. Actual prices may vary depending on the availability of ingredients and location-specific factors. We encourage readers to check local markets for the most current pricing information.**]''')

