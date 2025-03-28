import streamlit as st
import math

def calculator():
    """
    A Streamlit app for a comprehensive calculator with various functionalities,
    enhanced with styling for a more visually appealing experience.
    """

    # --- App Styling ---
    st.markdown(
        """
        <style>
        .reportview-container {
            background: linear-gradient(135deg, #e0f2f1, #fce4ec); /* Light Pastel Gradient */
        }
       .main .block-container {
          max-width: 800px;
        }

        .stButton>button {
            color: #fff;
            background-color: #4CAF50; /* Green */
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
        }

        .stSelectbox>label, .stNumberInput>label {
            color: #336699; /* Dark Blue */
            font-weight: bold;
        }

        .stSuccess {
            color: #2E7D32; /* Dark Green for Success Messages */
            background-color: #C8E6C9; /* Light Green Background */
            padding: 10px;
            border-radius: 5px;
        }

        .stError {
            color: #D32F2F; /* Dark Red for Error Messages */
            background-color: #FFCDD2; /* Light Red Background */
            padding: 10px;
            border-radius: 5px;
        }

        /* Adjust slider and input appearance */
        .stSlider>div>div>div>div {
            background-color: #29B6F6; /* Light Blue */
        }

        div.stNumberInput > label {
            font-size: 18px;
        }

        /* Make titles look nicer */
        h1, h2, h3, h4, h5, h6 {
            color: #2196F3; /* Blue */
            font-family: sans-serif;
        }

        div.block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- App Content ---
    st.title("🎨 Comprehensive Calculator")  # Added an emoji
    st.markdown("A versatile calculator with enhanced styling and functionalities.")

    # Input Section
    st.header("⚙️ Inputs") # Added an emoji

    calculation_type = st.selectbox(
        "Select Calculation Type:",
        [
            "Basic Arithmetic",
            "Scientific Calculations",
            "Unit Conversions",
            "Area Calculations",
            "Volume Calculations",
        ],
    )

    # 1. Basic Arithmetic
    if calculation_type == "Basic Arithmetic":
        st.subheader("➕ Basic Arithmetic") # Added an emoji
        num1 = st.number_input("Enter Number 1", value=0.0)
        num2 = st.number_input("Enter Number 2", value=0.0)
        operation = st.selectbox(
            "Select Operation:", ["Addition", "Subtraction", "Multiplication", "Division"]
        )

        if st.button("Calculate"):
            if operation == "Addition":
                result = num1 + num2
            elif operation == "Subtraction":
                result = num1 - num2
            elif operation == "Multiplication":
                result = num1 * num2
            elif operation == "Division":
                if num2 == 0:
                    result = "Error: Division by zero!"
                else:
                    result = num1 / num2
            st.success(f"✅ Result: {result}") # Added an emoji

    # 2. Scientific Calculations
    elif calculation_type == "Scientific Calculations":
        st.subheader("🔬 Scientific Calculations") # Added an emoji
        scientific_operation = st.selectbox(
            "Select Scientific Operation:",
            ["Square Root", "Exponentiation", "Logarithm", "Sine", "Cosine", "Tangent"],
        )
        num = st.number_input("Enter Number", value=1.0)

        if st.button("Calculate"):
            try:
                if scientific_operation == "Square Root":
                    result = math.sqrt(num)
                elif scientific_operation == "Exponentiation":
                    exponent = st.number_input("Enter Exponent", value=2.0)
                    result = num ** exponent
                elif scientific_operation == "Logarithm":
                    base = st.number_input("Enter Logarithm Base (default 10)", value=10.0)
                    if num <= 0:
                        result = "Error: Number must be positive for logarithm"
                    else:
                        result = math.log(num, base)
                elif scientific_operation == "Sine":
                    result = math.sin(math.radians(num))  # Convert to radians
                elif scientific_operation == "Cosine":
                    result = math.cos(math.radians(num))  # Convert to radians
                elif scientific_operation == "Tangent":
                    result = math.tan(math.radians(num))  # Convert to radians
                st.success(f"✅ Result: {result}") # Added an emoji

            except Exception as e:
                st.error(f"❌ Error: {e}") # Added an emoji

    # 3. Unit Conversions
    elif calculation_type == "Unit Conversions":
        st.subheader("📏 Unit Conversions") # Added an emoji
        conversion_type = st.selectbox(
            "Select Conversion Type:", ["Temperature", "Length", "Weight", "Currency"]
        )

        # Temperature Conversion
        if conversion_type == "Temperature":
            temp_value = st.number_input("Enter Temperature Value", value=0.0)
            from_unit = st.selectbox("From Unit:", ["Celsius", "Fahrenheit", "Kelvin"])
            to_unit = st.selectbox("To Unit:", ["Celsius", "Fahrenheit", "Kelvin"])

            if st.button("Convert"):
                if from_unit == to_unit:
                    result = temp_value
                elif from_unit == "Celsius" and to_unit == "Fahrenheit":
                    result = (temp_value * 9 / 5) + 32
                elif from_unit == "Celsius" and to_unit == "Kelvin":
                    result = temp_value + 273.15
                elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                    result = (temp_value - 32) * 5 / 9
                elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                    result = (temp_value - 32) * 5 / 9 + 273.15
                elif from_unit == "Kelvin" and to_unit == "Celsius":
                    result = temp_value - 273.15
                elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                    result = (temp_value - 273.15) * 9 / 5 + 32
                st.success(f"✅ Result: {result} {to_unit}") # Added an emoji

        # Length Conversion (Example)
        elif conversion_type == "Length":
             length_value = st.number_input("Enter Length Value", value=0.0)
             from_unit = st.selectbox("From Unit:", ["Meters", "Feet", "Inches", "Kilometers"])
             to_unit = st.selectbox("To Unit:", ["Meters", "Feet", "Inches", "Kilometers"])

             if st.button("Convert Length"):
                 if from_unit == to_unit:
                     result = length_value
                 elif from_unit == "Meters" and to_unit == "Feet":
                     result = length_value * 3.28084
                 elif from_unit == "Meters" and to_unit == "Inches":
                     result = length_value * 39.3701
                 elif from_unit == "Meters" and to_unit == "Kilometers":
                     result = length_value / 1000
                 elif from_unit == "Feet" and to_unit == "Meters":
                     result = length_value / 3.28084
                 elif from_unit == "Feet" and to_unit == "Inches":
                     result = length_value * 12
                 elif from_unit == "Feet" and to_unit == "Kilometers":
                     result = length_value / 3280.84
                 elif from_unit == "Inches" and to_unit == "Meters":
                     result = length_value / 39.3701
                 elif from_unit == "Inches" and to_unit == "Feet":
                     result = length_value / 12
                 elif from_unit == "Inches" and to_unit == "Kilometers":
                     result = length_value / 39370.1
                 elif from_unit == "Kilometers" and to_unit == "Meters":
                     result = length_value * 1000
                 elif from_unit == "Kilometers" and to_unit == "Feet":
                     result = length_value * 3280.84
                 elif from_unit == "Kilometers" and to_unit == "Inches":
                     result = length_value * 39370.1
                 st.success(f"✅ Result: {result} {to_unit}") # Added an emoji

        # You can add similar blocks for Weight and Currency conversions

    # 4. Area Calculations
    elif calculation_type == "Area Calculations":
        st.subheader("📐 Area Calculations") # Added an emoji
        shape = st.selectbox(
            "Select Shape:", ["Circle", "Rectangle", "Triangle"]
        )

        if shape == "Circle":
            radius = st.number_input("Enter Radius", value=1.0)
            if st.button("Calculate Area"):
                result = math.pi * radius**2
                st.success(f"✅ Area: {result}") # Added an emoji
        elif shape == "Rectangle":
            length = st.number_input("Enter Length", value=1.0)
            width = st.number_input("Enter Width", value=1.0)
            if st.button("Calculate Area"):
                result = length * width
                st.success(f"✅ Area: {result}") # Added an emoji
        elif shape == "Triangle":
            base = st.number_input("Enter Base", value=1.0)
            height = st.number_input("Enter Height", value=1.0)
            if st.button("Calculate Area"):
                result = 0.5 * base * height
                st.success(f"✅ Area: {result}") # Added an emoji

    # 5. Volume Calculations
    elif calculation_type == "Volume Calculations":
        st.subheader("📦 Volume Calculations") # Added an emoji
        shape = st.selectbox(
            "Select Shape:", ["Cube", "Sphere", "Cylinder"]
        )

        if shape == "Cube":
            side = st.number_input("Enter Side Length", value=1.0)
            if st.button("Calculate Volume"):
                result = side**3
                st.success(f"✅ Volume: {result}") # Added an emoji
        elif shape == "Sphere":
            radius = st.number_input("Enter Radius", value=1.0)
            if st.button("Calculate Volume"):
                result = (4/3) * math.pi * radius**3
                st.success(f"✅ Volume: {result}") # Added an emoji
        elif shape == "Cylinder":
            radius = st.number_input("Enter Radius", value=1.0)
            height = st.number_input("Enter Height", value=1.0)
            if st.button("Calculate Volume"):
                result = math.pi * radius**2 * height
                st.success(f"✅ Volume: {result}") # Added an emoji


if __name__ == "__main__":
    calculator()
