from openai import OpenAI

# Initializing the OpenAI client
client = OpenAI(api_key='my-api-key-here')

# Function to get completion from OpenAI
def get_completion(prompt, model="gpt-3.5-turbo"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Create a grocery shopping list?"},
            {"role": "user", "content": prompt},
        ]
    )
    return completion.choices[0].message.content

# Handling different options
option = input("What kind of grocery shopping list would you like to create this week?\n"
               "1. On a budget, I am limited on funds but would like to eat healthy\n"
               "2. I want to go all out!\n"
               "3. I need groceries with dietary restrictions\n"
               "Enter the number corresponding to your choice: ")

if option == "1":
    prompt = "Create a healthy budget friendly grocery shopping list for the week!"
    response = get_completion(prompt)
    print(response)

elif option == "2":
    prompt = "Give me an indulgent grocery shopping list for the week!"
    response = get_completion(prompt)
    print(response)

elif option == "3":
    prompt = "Can you create a grocery shopping list with dietary restrictions such as no meat or no pork"
    response = get_completion(prompt)
    print(response)

else:
    print("Invalid option. Please enter a number between 1 and 3.")

