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
    st.image("images/Spaghetti_Carbonara.jpg")
    carbonara = st.button("Spaghetti Carbonara")
    if carbonara: 
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Spaghetti Carbonara. Provide the number of servings, a list of ingredients ,and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Spaghetti Carbonara."
        response = get_completion(prompt)
        st.write(response)
    st.image("images/Chicken_Alfredo.jpg")
    alfredo = st.button("Chicken Alfredo")
    if alfredo:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Chicken Alfredo. Provide a list og ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Chicken Alfredo."
        response = get_completion(prompt)
        st.write(response)
    st.image("images/Pad_Thai.jpg")
    pad_thai = st.button("Pad Thai Noodles")
    if pad_thai:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Pad Thai Noodles. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Pad Thai Noodles."
        response = get_completion(prompt)
        st.write(response)

with cl2:
    st.image("images/Chicken_Tikka_Masala.jpg")
    tikka_masala = st.button("Chicken Tikka Masala")
    if tikka_masala:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Chicken Tikka Masala. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Chicken Tikka Masala."
        response = get_completion(prompt)
        st.write(response)
    st.image("images/California_Sushi.jpg")
    sushi = st.button("California Sushi Rolls")
    if sushi:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for California Sushi Rolls. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for California Sushi Rolls."
        response = get_completion(prompt)
        st.write(response)
    st.image("images/Tacos_Carne_Asada.jpg")
    tacos = st.button("Carne Asada Tacos")
    if tacos:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Carne Asada Tacos. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Carne Asada Tacos."
        response = get_completion(prompt)
        st.write(response)  

with cl3:
    st.image("images/Spanish_Paella.jpg")
    paella = st.button("Spanish Paella")
    if paella:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Spanish Paella. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Spanish Paella."
        response = get_completion(prompt)
        st.write(response)
    st.image("images/Falafel_Bowl.jpg")
    falafel = st.button("Falafel Bowl")
    if falafel:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Falafel Bowl. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Falafel Bowl."
        response = get_completion(prompt)
        st.write(response)
    st.image("images/Pesto_Pasta.jpg")
    pesto = st.button("Pesto Pasta")
    if pesto:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Pesto Pasta. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Pesto Pasta."
        response = get_completion(prompt)
        st.write(response)

with cl4:
    st.image("images/Stir_Fry.jpg")
    stir_fry = st.button("Chicken & Vegetable Stir Fry")
    if stir_fry:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Chicken & Vegetable Stir Fry. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Chicken & Vegetable Stir Fry."
        response = get_completion(prompt)
        st.write(response)
    st.image("images/Banana_Bread.jpg")
    banana_bread = st.button("Banana Bread")
    if banana_bread:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Banana Bread. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Banana Bread."
        response = get_completion(prompt)
        st.write(response)
    st.image("images/Barbeque Ribs.jpg")
    ribs = st.button("Barbeque Ribs")
    if ribs:
        def get_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for Barbeque Ribs. Provide a list of ingredients and steps to make the dish."},
                    {"role": "user",
                    "content": prompt},
                ]
            )
            return completion.choices[0].message.content
        prompt = "Provide a recipe for Barbeque Ribs."
        response = get_completion(prompt)
        st.write(response)

# Explore more recipes
st.subheader("Explore More Recipes")
recipe_question = st.text_input(label="Name of a Recipes:")
if st.button("Explore"):
    col1, col2 = st.columns([1, 0.5])
    with col1:
        st.subheader("Here is a recipe for " + recipe_question)
        def chat_completion(prompt, model="gpt-3.5-turbo"):
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role":"system",
                    "content": "Your job is to provide a recipe for the recipe name given in thee prompt. The recipe should list all ingredients and steps to prepare the dish. Use the format: a list of ingredients, and step by step instructions. Do not answer any other questions apart from recipe requests."},
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
        :red[**NOTE: This recipe is AI-generated and Budget Bite has not verified it for accuracy or safety. It may contain errors. Always use your best judgement when making AI-generated dishes.**]''')