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

# Define the layout
col1, col2 = st.columns([0.40, 4])
with col1:
    st.image("https://i.ibb.co/vDgcdkz/250x200.png")
with col2:
    st.header("AI-Powered Smart Meal Solutions for Students", divider="rainbow")

cl1, cl2 = st.columns([1, 1])
with cl1:
    st.image("images/Spaghetti_Carbonara.jpg")
    st.subheader("Spaghetti Carbonara")
    def get_completion(prompt, model="gpt-3.5-turbo"):
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role":"system",
                "content": "Your job is to provide a nutrition information for Spaghetti Carbonara. The information should include the both macro and micro nutrients. Use the USDA database for the nutritional information. The format of the output should be in a table with the following columns: Nutrient, Amount per serving, Daily Value. The daily value should be calculated based on a 2000 calorie diet."},
                {"role": "user",
                "content": prompt},
            ]
        )
        return completion.choices[0].message.content
    prompt = "Provide nutritional information for Spaghetti Carbonara."
    response = get_completion(prompt)
    st.write(response)
    

with cl2:
    def get_completion(prompt, model="gpt-3.5-turbo"):
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role":"system",
                "content": "Your job is to provide a recipe for Spaghetti Carbonara. Provide a list og ingredients and steps to make the dish."},
                {"role": "user",
                "content": prompt},
            ]
        )
        return completion.choices[0].message.content   
    prompt = "Provide a recipe for Spaghetti Carbonara."
    response = get_completion(prompt)
    st.write(response)

    