import os
import openai
import streamlit as st
from openai import OpenAI

st.markdown("Budget Bite")
st.sidebar.markdown("Budget Bite")

message = "Welcome to Budget Bite! \nSmart Meal Solutions for Students"
st.write(message)

# Create two radio buttons
weekly_budget = st.radio('Select Budget (per week)', ['$50', '$75', '$100'])
diet_type = st.radio('Diet Type', ['Vegan', 'Vegetarian', 'Non-Vegetarian', 'Gluten Free'])
dietary_preferneces = st.radio('Dietary Preferences', ['High Protien', 'High Fat', 'Balanced Nutrition'])

openai.api_key = os.environ["APIKEY"]

client = OpenAI()

# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": "Your job is to provide weekly meal plans for a budget of" + 
         weekly_budget +"that are" + diet_type + "and are" + dietary_preferneces + 
         "Please include the price for each ingredient and the nutrition content at the end"},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content

prompt = "Please provide weekly meal plan"

# create our streamlit app

with st.form("my_form"):
    #prompt = st.text_input("Enter a concept you would like me to explain: ") 
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write(get_completion(prompt))
