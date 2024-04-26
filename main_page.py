import os
import openai
import streamlit as st
from openai import OpenAI
import pandas as pd
import requests
import base64
from streamlit_navigation_bar import st_navbar
import navbar


#openai.api_key = os.environ["APIKEY"]
#client = OpenAI()

client = OpenAI(api_key='APIKEY')

# Set page config
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













# Define the layout
col1, col2 = st.columns([0.40, 4])
with col1:
    st.image("https://i.ibb.co/vDgcdkz/250x200.png")
with col2:
    st.header("AI-Powered Smart Meal Solutions for Students", divider="rainbow")

#st.markdown("----", unsafe_allow_html=True)
columns = st.columns((1.5, 3.5, 0.75))
with columns[1]:
    st.subheader("Generate a Recipe from Ingredients in Your Kitchen")
#st.markdown("----", unsafe_allow_html=True)

# Computer vision model
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

uploaded_file = st.file_uploader("Choose a picture file with available ingredient:", type=["png", "jpg", "jpeg"])

image_path = "images/Stir_Fry.jpg"

def photo_rec(image_path):
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What’s in this image in terms of food?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content

    

if uploaded_file is not None:
    with open(os.path.join('images',uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    #st.success("Saved File:{} to images".format(uploaded_file.name))
    image_path = os.path.join('images',uploaded_file.name)
    #st.image(image_path)
    content = photo_rec(image_path)
    #st.write(content)

    ingredient_list = content
    colmn1, colmn2, colmn3 = st.columns(3)
    with colmn1:
        st.write("Here's a recipe inspiration for you:")
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
        recipe = get_completion(ingredient_list)
        st.write(recipe)

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

    with colmn2:
        response = client.images.generate(
            model="dall-e-2",
            prompt=recipe_name,
            size="512x512",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        st.image(image_url, caption=recipe_name, use_column_width=True)

    with colmn3:
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

        st.write(get_nutrition(recipe))
    st.markdown('''
        :red[**NOTE: This recipe is AI-generated and Budget Bite has not verified it for accuracy or safety. It may contain errors. Always use your best judgement when making AI-generated dishes.**]''')
    
columns = st.columns((4, 1, 4))
with columns[1]:
    st.write("**Or**")

# Generate a recipe from ingredients
    
ingredient_list_prompt = st.text_input(label="Enter a list of available ingredients separated by commas:")
columns = st.columns((9, 0.8))
button_pressed = columns[1].button('Generate')
if button_pressed:
    cln1, cln2, cln3 = st.columns(3)
    with cln1:
        st.write("Here's a recipe inspiration for you:")
        # create a wrapper function
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                {"role":"system",
                "content": "Your job is to provide a recipe for the ingredients mentioned in the prompt. The recipe should list all ingredients and steps to prepare the dish. Use the format: Name of the recipe, a list of ingredients, and step by step instructions."},
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
        st.markdown('''
        :red[**NOTE: This recipe is AI-generated and Budget Bite has not verified it for accuracy or safety. It may contain errors. Always use your best judgement when making AI-generated dishes.**]''')

st.subheader("Try our popular recipes!")

column1, column2, column3, column4 = st.columns(4)
with column1:
    st.image("images/Quinoa_Tabbouleh.jpg")
    quinoa = st.button("Quinoa Tabbouleh")
    if quinoa:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for quinoa tabbouleh. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Quinoa Tabbouleh."
        response = get_completion(prompt)
        st.write(response)
        
        
    
with column2:
    st.image("images/Pistachio-Crusted_Baked_Salmon.jpg")
    salmon = st.button("Pistachio-Crusted Baked Salmon")
    if salmon:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for pistachio-crusted baked salmon. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Pistachio-Crusted Baked Salmon."
        response = get_completion(prompt)
        st.write(response)

with column3:
    st.image("images/Decadent_Fudge_Brownies.jpg")
    brownies = st.button("Decadent Fudge Brownies")
    if brownies:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for decadent fudge brownies. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Decadent Fudge Brownies."
        response = get_completion(prompt)
        st.write(response)

with column4:
    st.image("images/Sheet_Pan_Chicken_Fajitas.jpg")
    fajitas = st.button("Sheet Pan Chicken Fajitas")
    if fajitas:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for sheet pan chicken fajitas. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Sheet Pan Chicken Fajitas."
        response = get_completion(prompt)
        st.write(response)

    