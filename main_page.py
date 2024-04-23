import os
import openai
import streamlit as st
from openai import OpenAI
import pandas as pd
import requests

#openai.api_key = os.environ["APIKEY"]

#client = OpenAI()
client = OpenAI(api_key="APIKEY")




import streamlit as st

def main():
    # Set the page configuration as the very first command
    st.set_page_config(layout="wide")

    # Custom CSS to overwrite Streamlit's default settings
    st.markdown(
        '''
        <style>
            .css-18e3th9 {
                background-color: #f0fff4; /* Light green background */
            }
            .css-1d391kg {
                color: #006400; /* Dark green text for titles */
            }
            .stButton>button {
                color: white;
                background-color: #32cd32; /* Lime Green button */
            }
            .stRadio>label {
                color: #2e8b57; /* Sea Green text for radio buttons */
            }
            .stMultiSelect>div>div {
                background-color: #8fbc8f; /* Dark Sea Green background for multi-select */
            }
        </style>
        ''',
        unsafe_allow_html=True
    )

    st.image("https://i.ibb.co/vDgcdkz/250x200.png")
with col2:
    st.header("AI-Powered Smart Meal Solutions for Students", divider="rainbow")

 
st.subheader("Generate a Recipe from Ingredients in Your Kitchen")
subheader_alignment = """
<style>
#the-subheader {
    text-align: center
}
</style>
"""
st.markdown(subheader_alignment, unsafe_allow_html=True)

ingredient_list_prompt = st.text_input(label="Please enter a list of ingredients separated by commas:")
if st.button("Generate"):
    cln1, cln2, cln3 = st.columns(3)
    with cln1:
        st.write("Here's a recipe inspiration for you:")
        # create a wrapper function
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                {"role":"system",
                "content": "Step1: Your job is to provide a recipe for the ingredients mentioned in the prompt. The recipe should list all ingredients and steps to prepare the dish. Use the format: Name of the recipe, a list of ingredients, and step by step instructions."},
                {"role": "user",
                "content":prompt},
                ]
            )
            return completion.choices[0].message.content
        recipe = get_completion(ingredient_list_prompt)
        st.write(recipe)

        # get recipe name
        def get_recipe_name(prompt):
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                {"role":"system",
                "content": "Your job is to provide the name of the recipe from the given recipe. The output should be just the name of the recipe, exclude the ingredients or instructions. Only return the name of the recipe."},
                {"role": "user",
                "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        recipe_name = get_recipe_name(recipe)

    with cln2:
        # generate image for the recipe
        response = client.images.generate(
            model="dall-e-2",
            prompt=recipe_name,
            size="512x512",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        st.image(image_url, caption=recipe_name, use_column_width=True)

    with cln3: 
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
    
        prompt = get_nutrition(recipe)
        st.write(get_nutrition(prompt))
        st.write("NOTE: This recipe is AI-generated and Budget Bite has not verified it for accuracy or safety. It may contain errors. Always use your best judgement when making AI-generated dishes.")


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
        
