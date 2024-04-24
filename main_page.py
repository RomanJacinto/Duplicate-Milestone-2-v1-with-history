import os
import openai
import streamlit as st
from openai import OpenAI
import pandas as pd
import requests
import base64

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

# Set page config
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Define the background style using a direct image URL
#background_url = "https://i.imgur.com/ycNTyh7.png"

#background_style = f"""
#<style>
    #.stApp {{
        #background-image: url('{background_url}');
        #background-size: cover;
        #background-position: center;
    #}}
#</style>
#"""

# Apply the background style to the app
#st.markdown(background_style, unsafe_allow_html=True)

# Define the layout
col1, col2 = st.columns([0.40, 4])
with col1:
    st.image("https://i.ibb.co/vDgcdkz/250x200.png")
with col2:
    st.header("AI-Powered Smart Meal Solutions for Students", divider="rainbow")

# Computer vision model
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

uploaded_file = st.file_uploader("Choose a picture file", type=["png", "jpg", "jpeg"])

image_path = "images/cloud.png"

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
    st.success("Saved File:{} to images".format(uploaded_file.name))
    image_path = os.path.join('images',uploaded_file.name)
    st.image(image_path)
    content = photo_rec(image_path)
    st.write(content)
 
st.subheader("Generate a Recipe from Ingredients in Your Kitchen")

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
        st.markdown('''
        :red[**NOTE: This recipe is AI-generated and Budget Bite has not verified it for accuracy or safety. It may contain errors. Always use your best judgement when making AI-generated dishes.**]''')


