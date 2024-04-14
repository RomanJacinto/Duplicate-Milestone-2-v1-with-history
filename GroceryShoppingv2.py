import streamlit as st
import openai

st.markdown("Grocery Shopping List Generator")
st.sidebar.markdown("Grocery Shopping List Generator")

message = "Experience the magical grocery generator! \nWhere students can create a shopping list based on personal needs!"
st.write(message)

def generate_grocery_list(weeks, vegetarian=False):
    # Base ingredients
    ingredients = {
        "eggs": 2,
        "spinach": 50,
        "mushrooms": 50,
        "avocado": 0.5,
        "bread": 1,
        "chicken_breast": 200 if not vegetarian else 0,
        "mixed_salad_greens": 100,
        "nuts": 30,
        "vegetables": 200,
        "broccoli": 100,
        "carrots": 100
    }
    
    # Calculate total ingredients needed for specified weeks
    total_ingredients = {key: value * 7 * weeks for key, value in ingredients.items()}
    return total_ingredients

def get_openai_tip(query):
    openai.api_key = st.secrets["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"]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=query,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit application layout
st.title("Grocery List Generator")

# Inputs
weeks = st.number_input("Enter the number of weeks for the grocery list:", min_value=1, value=4)
vegetarian = st.checkbox("Vegetarian Option")

# Generate Button
if st.button("Generate Grocery List"):
    grocery_list = generate_grocery_list(weeks, vegetarian)
    st.subheader("Grocery List:")
    for ingredient, quantity in grocery_list.items():
        if quantity > 0:  # Only display if needed
            st.write(f"{ingredient.title()}: {quantity} units")

    # Optional OpenAI tip
    if st.button("Get Cooking Tips"):
        tip = get_openai_tip("Provide some cooking tips for a healthy vegetarian diet")
        st.write(tip)
