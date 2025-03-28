import streamlit as st
import math
import numpy as np
import random

def calculator():
    """
    A Streamlit app with a Pokémon background image and engaging examples.
    """

    # --- Helper Functions (Same as Before) ---
    def generate_addition_example(num1, num2, result):
        items = ["Poké Balls", "Potions", "Berries", "Badges", "Rare Candies"]
        item = random.choice(items)
        verbs = ["caught", "found", "received", "picked up"]
        verb = random.choice(verbs)

        return f"You had {num1} {item} and {verb} {num2} more. Now you have {result} {item}."

    def generate_subtraction_example(num1, num2, result):
        items = ["Pokémon cards", "Trainer Tips", "Evolution Stones", "Super Potions"]
        item = random.choice(items)
        verbs = ["lost", "traded", "gave away", "used", "sold"]
        verb = random.choice(verbs)

        return f"You started with {num1} {item} and {verb} {num2} of them.  You now have {result} {item} left."

    def generate_multiplication_example(num1, num2, result):
        groups = ["packs", "boxes", "sets", "decks"]
        group = random.choice(groups)
        items = ["trainer cards", "energy cards", "Pokémon figurines"]
        item = random.choice(items)

        return f"You have {num1} {group} of {item}, and each {group} contains {num2} {item}.  So you have a total of {result} {item}."

    def generate_division_example(num1, num2, result):
        items = ["rare candies", "TMs", "evolution stones", "berries"]
        item = random.choice(items)
        people = ["team members", "gym trainers", "fellow trainers", "friends"]
        person = random.choice(people)

        return f"You have {num1} {item} to share equally among {num2} {person}. Each person gets {result} {item}."

    # --- App Styling ---
    pokemon_image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png" #Example Pokemon Pikachu Image

    st.markdown(
        f"""
        <style>
        body {{
            background-image: url("{pokemon_image_url}"); /* Replace with your Pokémon image URL */
            background-size: cover; /* Cover the entire background */
            background-repeat: no-repeat; /* Prevent image from repeating */
            background-attachment: fixed; /* Keep the background fixed during scrolling */
            color: white; /* Set default text color to white for better contrast */
        }}
        .reportview-container {{
            background: transparent; /* Make the container transparent */
        }}
        .main {{
            background: transparent; /* Make the main area transparent */
            max-width: 800px; /* Limit width */
            margin: 0 auto; /* Center the app */
        }}
        .block-container {{
          background-color: rgba(255, 255, 255, 0.1); /* Add a semi-transparent white container */
          padding: 20px;
          border-radius: 10px;
        }}

        .stButton>button {{
            color: #fff;
            background-color: #d81b60; /* Darker Pink */
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Add a subtle shadow */
        }}

        .stButton>button:hover {{
            background-color: #c2185b;  /* Slightly darker pink on hover */
        }}

        .stSelectbox>label, .stNumberInput>label {{
            color: #f8bbd0; /* Light Pink */
            font-weight: bold;
        }}

        .stSuccess {{
            color: #e91e63; /* Pink */
            background-color: #fce4ec; /* Very Light Pink Background */
            padding: 10px;
            border-radius: 5px;
        }}

        .stError {{
            color: #673ab7; /* Purple */
            background-color: #ede7f6; /* Very Light Purple Background */
            padding: 10px;
            border-radius: 5px;
        }}

        /* Adjust slider and input appearance */
        .stSlider>div>div>div>div {{
            background-color: #ba68c8; /* Lavender */
        }}

        div.stNumberInput > label {{
            font-size: 18px;
        }}

        /* Make titles look nicer */
        h1, h2, h3, h4, h5, h6 {{
            color: #ce93d8; /* Light Purple */
            font-family: sans-serif;
        }}

        /* Card Styling */
        .card {{
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- App Content ---
    st.title("🔢 Math Explorer: Gotta Calculate 'Em All!")
    st.markdown("A fun calculator with Pokémon! Enter whole numbers only.")

    # Input Section
    st.header("🎮 Let's Calculate!")

    calculation_type = st.selectbox(
        "Choose your adventure:",
        [
            "Basic Arithmetic",
        ],
    )

    # 1. Basic Arithmetic
    if calculation_type == "Basic Arithmetic":
        st.subheader("🍎 Basic Arithmetic Adventures")
        st.write("Add, subtract, multiply, or divide whole numbers. Let's make it a Pokémon training session!")

        with st.container(): # Using container to create a "card" effect
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            num1 = st.number_input("Enter First Number (Whole Number)", value=0, step=1) #step=1 ensures whole numbers
            st.markdown("</div>", unsafe_allow_html=True)

        with st.container(): # Using container to create a "card" effect
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            num2 = st.number_input("Enter Second Number (Whole Number)", value=0, step=1)
            st.markdown("</div>", unsafe_allow_html=True)

        operation = st.selectbox(
            "Select Operation:", ["Addition", "Subtraction", "Multiplication", "Division"]
        )

        if st.button("Do the Math!"):
            if operation == "Addition":
                result = num1 + num2
                example = generate_addition_example(num1, num2, result)
            elif operation == "Subtraction":
                result = num1 - num2
                example = generate_subtraction_example(num1, num2, result)
            elif operation == "Multiplication":
                result = num1 * num2
                example = generate_multiplication_example(num1, num2, result)
            elif operation == "Division":
                if num2 == 0:
                    result = "Error: Division by zero!"
                    example = None
                else:
                    result = num1 // num2 #Integer Division
                    remainder = num1 % num2

                    if remainder != 0:
                        example = generate_division_example(num1, num2, result) + f" (with {remainder} left over)."
                    else:
                        example = generate_division_example(num1, num2, result)

                    result = f"{result}" #Displaying integer quotient



            if example:
                st.success(f"🎉 Result: {result}")
                st.info(example)
            else:
                st.error(result)
                st.stop()


if __name__ == "__main__":
    calculator()
