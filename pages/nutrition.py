import os
import openai
import streamlit as st
from openai import OpenAI

st.image("/Users/kulsoom/Milestone-2-v1/Milestone-2-v1/static/download.jpeg")

client = OpenAI(api_key='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')

def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": "Your job is to information about nutrition health and dietary choices."},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content


option = st.selectbox(
   "What would you like to learn about?",
   ("Importance of Balance", "Why are proteins important?", "Which Veggies?"),
   index=None,
   placeholder="Select a tab and start exploring",
)

if (option == "Importance of Balance"):
    prompt = "Please explain the importance of eating balanced and healthy meals"

    response = get_completion(prompt)


    st.write(response)

elif (option == "Why are proteins important?"):
    prompt = "Please explain the importance of eating balanced and healthy meals"

    response = get_completion(prompt)

    st.write(response)

elif (option == "Which Veggies?"):
    prompt = "Please explain the importance of eating balanced and healthy meals"

    response = get_completion(prompt)

    st.write(response)


