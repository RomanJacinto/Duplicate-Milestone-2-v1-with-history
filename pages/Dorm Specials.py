import os
import openai
import streamlit as st
from openai import OpenAI
import pandas as pd
import requests
import base64

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

# Set page title and favicon.
st.set_page_config(layout="wide")
#create columns for welcome message and logo
col1, col2 = st.columns([0.40, 4])
with col1:
    st.image("https://i.ibb.co/vDgcdkz/250x200.png")
with col2:
    st.header("AI-Powered Smart Meal Solutions for Students", divider="rainbow")

cl1, cl2, cl3, cl4 = st.columns([1, 1, 1, 1])
with cl1:
    st.image("images_dorm_recipes/Mac & Cheese.jpg")
    mac_cheese = st.button("Microwave Mac & Cheese")
    if mac_cheese: 
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Microwave Mac & Cheese that can be made in a dorm. Provide a list of ingredients ,and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Microwave Mac & Cheese."
        response = get_completion(prompt)
        st.write(response)
    st.image("images_dorm_recipes/Upgraded_Ramen_Noodles.jpg")
    ramen = st.button("Upgraded Ramen Noodles")
    if ramen:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Upgraded Ramen Noodles, made with vegetables, garnished with baby spinach leaves, and topped with microwaved fried egg that can be made in a dorm. Provide a list of ingredients ,and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Upgraded Ramen Noodles."
        response = get_completion(prompt)
        st.write(response)
    st.image("images_dorm_recipes/Easy_Quesadillas.jpg")
    quesadillas = st.button("Easy Quesadillas")
    if quesadillas:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Easy Quesadillas that can be made in a dorm. Provide a list of ingredients ,and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Easy Quesadillas."
        response = get_completion(prompt)
        st.write(response)

with cl2:
    st.image("images_dorm_recipes/Greek_Yogurt_Parfaits.jpg")
    parfaits = st.button("Greek Yogurt Parfaits")
    if parfaits:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Greek Yogurt Parfaits that can be made in a dorm. Provide a list of ingredients ,and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Greek Yogurt Parfaits."
        response = get_completion(prompt)
        st.write(response)
    st.image("images_dorm_recipes/Overnight_Oats.jpg")
    oats = st.button("Overnight Oats")
    if oats:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Overnight Oats that can be made in a dorm. Provide a list of ingredients ,and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Overnight Oats."
        response = get_completion(prompt)
        st.write(response)
    st.image("images_dorm_recipes/Rice_Cooker_Pasta.jpg")
    pasta = st.button("Rice Cooker Pasta")
    if pasta:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Rice Cooker Pasta that can be made in a dorm. Provide a list of ingredients ,and steps to make the dish. Suggest to user to use their favorite pasta sauce and add some vegetables for a balanced meal."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Rice Cooker Pasta."
        response = get_completion(prompt)
        st.write(response)

with cl3:
    st.image("images_dorm_recipes/Microwave_Red_Velvet_Cookie.jpg")
    cookie = st.button("Microwave Red Velvet Cookie")
    if cookie:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Microwave Red Velvet Cookie that can be made in a dorm. Provide a list of ingredients ,and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Microwave Red Velvet Cookie."
        response = get_completion(prompt)
        st.write(response)
    st.image("images_dorm_recipes/Easy_Greek_Salad.jpg")
    salad = st.button("Easy Greek Salad")
    if salad:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Easy Greek Salad that can be made in a dorm. Provide a list of ingredients ,and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Easy Greek Salad."
        response = get_completion(prompt)
        st.write(response)
    st.image("images_dorm_recipes/Microwave_Pancakes.jpg")
    pancakes = st.button("Microwave Pancakes")
    if pancakes:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Microwave Pancakes that can be made in a dorm. Provide a list of ingredients ,and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Microwave Pancakes."
        response = get_completion(prompt)
        st.write(response)
with cl4:
    st.image("images_dorm_recipes/Avocado_Tuna_Sandwich.jpg")
    sandwich = st.button("Avocado Tuna Sandwich")
    if sandwich:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Avocado Tuna Sandwich that can be made in a dorm. Provide a list of ingredients ,and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Avocado Tuna Sandwich."
        response = get_completion(prompt)
        st.write(response)
    st.image("images_dorm_recipes/Microwave_Chocolate_Mug_Cake.jpg")
    cake = st.button("Microwave Chocolate Mug Cake")
    if cake:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Microwave Chocolate Mug Cake that can be made in a dorm. Provide a list of ingredients ,and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Microwave Chocolate Mug Cake."
        response = get_completion(prompt)
        st.write(response)
    st.image("images_dorm_recipes/Pasta_Salad.jpg")
    pasta_salad = st.button("Pasta Salad")
    if pasta_salad:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Pasta Salad that can be made in a dorm. Provide a list of ingredients ,and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Pasta Salad."
        response = get_completion(prompt)
        st.write(response)

# Explore more Dorm specials recipes
st.subheader("Explore more Dorm Specials Recipes")
recipe_question = st.text_input(label="Look for more Dorm Specials Recipes:")
if st.button("Explore"):
    col1, col2 = st.columns([1, 0.5])
    with col1:
        st.subheader("Here is a recipe for " + recipe_question)
        def chat_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe that can be made in a dorm room using microwave, boiler plate, or rice cooker. The recipe should list all ingredients and steps to prepare the dish. Use the format: a list of ingredients, and step by step instructions. Do not answer any other questions apart from recipe requests."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "please provide a recipe for " + recipe_question
        response = chat_completion(prompt)
        st.write(response)
    with col2:
        # generate image for the recipe
        response = client.images.generate(
            model="dall-e-2",
            prompt=recipe_question + "styled for a recipes website",
            size="512x512",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url
        st.image(image_url, caption=recipe_question, use_column_width=True)


st.markdown('''
        :red[**NOTE: This recipe is AI-generated and Budget Bite has not verified it for accuracy or safety. It may contain errors. Always use your best judgement when making AI-generated recipes.**]''')
