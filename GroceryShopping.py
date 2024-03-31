import os
import openai
import streamlit as st
from openai import OpenAI

st.markdown("Grocery Shopping List Generator")
st.sidebar.markdown("Grocery Shopping List Generator")

message = "Experience the magical grocery generator! \nWhere students can create a shopping list based on personal needs!"
st.write(message)

client = OpenAI(api_key="APIKEY")

def grocery_list():
    st.title("My Grocery List")
    
    # Initialize an empty list to store groceries
    groceries = []
    
    # Text input to add items to the list
    new_item = st.text_input("Add new item:")
    
    # Button to add the item to the list
    if st.button("Add"):
        if new_item:
            groceries.append(new_item)
            st.success(f"'{new_item}' added to the list!")
        else:
            st.warning("Please enter an item.")
    
    # Display the current grocery list
    st.subheader("Current Grocery List:")
    for i, item in enumerate(groceries, start=1):
        st.write(f"{i}. {item}")

if __name__ == "__main__":
    grocery_list()
