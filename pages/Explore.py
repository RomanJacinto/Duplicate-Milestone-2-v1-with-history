import os
import openai
import streamlit as st
from openai import OpenAI
import pandas as pd
import requests

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
        link = '[GitHub](http://github.com)'
        st.markdown(link, unsafe_allow_html=True)
       
