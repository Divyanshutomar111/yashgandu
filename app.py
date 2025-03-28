import streamlit as st
import math
import numpy as np
import random

def calculator():
    """
    A Streamlit app for a comprehensive calculator with enhanced UI, integer-only input,
    engaging examples, and optimized code.
    """

    # --- Helper Functions ---
    def generate_addition_example(num1, num2, result):
        items = ["apples", "bananas", "candies", "books", "toys", "marbles"]
        item = random.choice(items)
        verbs = ["gave", "found", "received", "picked up"]
        verb = random.choice(verbs)

        return f"You had {num1} {item} and {verb} {num2} more. Now you have {result} {item}."

    def generate_subtraction_example(num1, num2, result):
        items = ["cookies", "balloons", "pencils", "stickers", "flowers", "chocolates"]
        item = random.choice(items)
        verbs = ["ate", "lost", "gave away", "broke", "sold"]
        verb = random.choice(verbs)

        return f"You started with {num1} {item} and {verb} {num2} of them.  You now have {result} {item} left."

    def generate_multiplication_example(num1, num2, result):
        groups = ["boxes", "bags", "stacks", "rows", "sets", "piles"]
        group = random.choice(groups)
        items = ["cards", "beads", "coins", "pebbles", "buttons"]
        item = random.choice(items)

        return f"You have {num1} {group} of {item}, and each {group} contains {num2} {item}.  So you have a total of {result} {item}."

    def generate_division_example(num1, num2, result):
        items = ["slices of pizza", "cupcakes", "portions of food", "paper clips", "rubber bands"]
        item = random.choice(items)
        people = ["friends", "colleagues", "classmates", "family members"]
        person = random.choice(people)

        return f"You have {num1} {item} to share equally among {num2} {person}. Each person gets {result} {item}."

    # --- App Styling ---
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(135deg, #e91e63, #673ab7); /* Pink to Purple Gradient */
            color: white; /* Set default text color to white for better contrast */
        }
        .reportview-container {
            background: transparent; /* Make the container transparent */
        }
        .main {
            background: transparent; /* Make the main area transparent */
            max-width: 800px; /* Limit width */
            margin: 0 auto; /* Center the app */
        }
        .block-container {
          background-color: rgba(255, 255, 255, 0.1); /* Add a semi-transparent white container */
          padding: 20px;
          border-radius: 10px;
        }

        .stButton>button {
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
        }

        .stButton>button:hover {
            background-color: #c2185b;  /* Slightly darker pink on hover */
        }

        .stSelectbox>label, .stNumberInput>label {
            color: #f8bbd0; /* Light Pink */
            font-weight: bold;
        }

        .stSuccess {
            color: #e91e63; /* Pink */
            background-color: #fce4ec; /* Very Light Pink Background */
            padding: 10px;
            border-radius: 5px;
        }

        .stError {
            color: #673ab7; /* Purple */
            background-color: #ede7f6; /* Very Light Purple Background */
            padding: 10px;
            border-radius: 5px;
        }

        /* Adjust slider and input appearance */
        .stSlider>div>div>div>div {
            background-color: #ba68c8; /* Lavender */
        }

        div.stNumberInput > label {
            font-size: 18px;
        }

        /* Make titles look nicer */
        h1, h2, h3, h4, h5, h6 {
            color: #ce93d8; /* Light Purple */
            font-family: sans-serif;
        }

        /* Card Styling */
        .card {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- App Content ---
    st.title("🔢 Math Explorer")
    st.markdown("A fun calculator with stories! Enter whole numbers only.")

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
        st.write("Add, subtract, multiply, or divide whole numbers. Let's make it a story!")

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
