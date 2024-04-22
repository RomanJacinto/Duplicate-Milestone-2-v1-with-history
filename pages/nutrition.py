import os
import openai
import streamlit as st
from openai import OpenAI


client = OpenAI(api_key='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')

# Custom HTML/CSS for the banner
custom_html = """
<div class="banner">
    <img src="https://t4.ftcdn.net/jpg/02/70/48/37/360_F_270483752_utMOlYHyqko8LLdeVdlrx5WjHqQocCbM.jpg" alt="Banner Image">
</div>

<style>
    .banner {
        width: 100%;
        height: 400px;
        overflow: hidden;
    }
    .banner img {
        width: 100%;
        object-fit: cover;
    }
</style>
"""
# Display the custom HTML
st.components.v1.html(custom_html)



def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": "Your job is to information about nutrition health and dietary choices. You cannot address any questions that do not pertain to nutrition and education. If any such question is asked of you, reply 'I cannot answer that question. Try asking me something about dietary needs and education!'"},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content

st.header("Learn about Nutrition and Dietary Choices!")

questions = st.text_input(label="Ask a question about nutrition")
  

if st.button("Ask"):
    response = get_completion(questions)
    st.write(response)





