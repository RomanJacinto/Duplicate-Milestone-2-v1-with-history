import streamlit as st

def home():
    st.page_link("main_page.py", label="Home")

def mealplan():
    st.switch_page("pages/Budgeted Meal Plans.py")

def dorm():
    st.switch_page("pages/Dorm Specials.py")

def explore():
    st.switch_page("pages/Explore Recipes.py")

def bank():
    st.switch_page("pages/Nearest Food Bank.py")

def learn():
    st.switch_page("pages/nutrition.py")