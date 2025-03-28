import streamlit as st
import math
import numpy as np  # For complex number support

def calculator():
    """
    A Streamlit app for a comprehensive calculator with enhanced UI, complex number support,
    detailed examples, and optimized code.
    """

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

        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- App Content ---
    st.title("⚛️ Comprehensive Calculator")
    st.markdown("A versatile calculator with a stylish theme, complex number support, and detailed examples.")

    # Input Section
    st.header("⚙️ Inputs")

    calculation_type = st.selectbox(
        "Select Calculation Type:",
        [
            "Basic Arithmetic",
            "Scientific Calculations",
            "Complex Number Operations",
            "Unit Conversions",
            "Area Calculations",
            "Volume Calculations",
        ],
    )

    # 1. Basic Arithmetic
    if calculation_type == "Basic Arithmetic":
        st.subheader("➕ Basic Arithmetic")
        st.write("Perform basic calculations. Supports real and complex numbers.")
        num1 = st.text_input("Enter Number 1 (e.g., 2+3j or 2)", value="0")
        num2 = st.text_input("Enter Number 2 (e.g., 4-1j or 4)", value="0")
        operation = st.selectbox(
            "Select Operation:", ["Addition", "Subtraction", "Multiplication", "Division"]
        )

        try:
            num1 = complex(num1)
            num2 = complex(num2)
            if st.button("Calculate"):
                if operation == "Addition":
                    result = num1 + num2
                    example = f"Example: ({num1}) + ({num2}) = {result}"
                elif operation == "Subtraction":
                    result = num1 - num2
                    example = f"Example: ({num1}) - ({num2}) = {result}"
                elif operation == "Multiplication":
                    result = num1 * num2
                    example = f"Example: ({num1}) * ({num2}) = {result}"
                elif operation == "Division":
                    if num2 == 0:
                        result = "Error: Division by zero!"
                        example = None
                    else:
                        result = num1 / num2
                        example = f"Example: ({num1}) / ({num2}) = {result}"

                if example:
                    st.success(f"✅ Result: {result}")
                    st.info(example)
                else:
                    st.error(result)

        except ValueError:
            st.error("Invalid input. Please enter numbers (real or complex).")

    # 2. Scientific Calculations
    elif calculation_type == "Scientific Calculations":
        st.subheader("🔬 Scientific Calculations")
        st.write("Calculate advanced functions. Supports real numbers.")
        operation = st.selectbox(
            "Select Operation:",
            ["Square Root", "Exponentiation", "Logarithm", "Sine", "Cosine", "Tangent"],
        )
        num = st.number_input("Enter Number", value=1.0)

        if st.button("Calculate"):
            try:
                if operation == "Square Root":
                    if num < 0:
                        result = "Error: Cannot calculate square root of a negative real number."
                        example = None
                    else:
                        result = math.sqrt(num)
                        example = f"Example: √({num}) = {result}"
                elif operation == "Exponentiation":
                    exponent = st.number_input("Enter Exponent", value=2.0)
                    result = num ** exponent
                    example = f"Example: {num}^{exponent} = {result}"
                elif operation == "Logarithm":
                    base = st.number_input("Enter Logarithm Base (default 10)", value=10.0)
                    if num <= 0:
                        result = "Error: Number must be positive for logarithm"
                        example = None
                    else:
                        result = math.log(num, base)
                        example = f"Example: log{base}({num}) = {result}"
                elif operation == "Sine":
                    result = math.sin(math.radians(num))
                    example = f"Example: sin({num} degrees) = {result}"
                elif operation == "Cosine":
                    result = math.cos(math.radians(num))
                    example = f"Example: cos({num} degrees) = {result}"
                elif operation == "Tangent":
                    result = math.tan(math.radians(num))
                    example = f"Example: tan({num} degrees) = {result}"

                if example:
                    st.success(f"✅ Result: {result}")
                    st.info(example)
                else:
                    st.error(result)

            except ValueError as e:
                st.error(f"Error: {e}")

    # 3. Complex Number Operations
    elif calculation_type == "Complex Number Operations":
        st.subheader("🧮 Complex Number Operations")
        st.write("Perform advanced operations on complex numbers.")

        complex_op = st.selectbox(
            "Select Operation:",
            ["Absolute Value", "Conjugate", "Real Part", "Imaginary Part", "Angle (Phase)"]
        )
        num_str = st.text_input("Enter Complex Number (e.g., 3+4j)", value="0")

        try:
            num = complex(num_str)
            if st.button("Calculate Complex"):
                if complex_op == "Absolute Value":
                    result = abs(num)
                    example = f"Example: |{num}| = {result}"
                elif complex_op == "Conjugate":
                    result = num.conjugate()
                    example = f"Example: Conjugate of {num} is {result}"
                elif complex_op == "Real Part":
                    result = num.real
                    example = f"Example: Real part of {num} is {result}"
                elif complex_op == "Imaginary Part":
                    result = num.imag
                    example = f"Example: Imaginary part of {num} is {result}"
                elif complex_op == "Angle (Phase)":
                    result = np.angle(num)  # Returns angle in radians
                    result_degrees = np.degrees(result)  # Convert to degrees
                    example = f"Example: Angle of {num} is {result_degrees} degrees"
                    result = result_degrees  # Display in degrees

                st.success(f"✅ Result: {result}")
                st.info(example)

        except ValueError:
            st.error("Invalid complex number format.  Use 'a+bj' or 'a-bj'.")

    # 4. Unit Conversions
    elif calculation_type == "Unit Conversions":
        st.subheader("📏 Unit Conversions")
        st.write("Convert between units of measurement.")

        conversion_type = st.selectbox(
            "Select Conversion Type:", ["Temperature", "Length"]  # Removed Currency for simplicity
        )

        # Temperature Conversion
        if conversion_type == "Temperature":
            temp_value = st.number_input("Enter Temperature Value", value=0.0)
            from_unit = st.selectbox("From Unit:", ["Celsius", "Fahrenheit", "Kelvin"])
            to_unit = st.selectbox("To Unit:", ["Celsius", "Fahrenheit", "Kelvin"])

            if st.button("Convert"):
                if from_unit == to_unit:
                    result = temp_value
                    example = f"{temp_value} {from_unit} is the same as {temp_value} {to_unit}."
                elif from_unit == "Celsius" and to_unit == "Fahrenheit":
                    result = (temp_value * 9 / 5) + 32
                    example = f"Example: ({temp_value}°C * 9/5) + 32 = {result}°F"
                elif from_unit == "Celsius" and to_unit == "Kelvin":
                    result = temp_value + 273.15
                    example = f"Example: {temp_value}°C + 273.15 = {result}K"
                elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                    result = (temp_value - 32) * 5 / 9
                    example = f"Example: ({temp_value}°F - 32) * 5/9 = {result}°C"
                elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                    result = (temp_value - 32) * 5 / 9 + 273.15
                    example = f"Example: (({temp_value}°F - 32) * 5/9) + 273.15 = {result}K"
                elif from_unit == "Kelvin" and to_unit == "Celsius":
                    result = temp_value - 273.15
                    example = f"Example: {temp_value}K - 273.15 = {result}°C"
                elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                    result = (temp_value - 273.15) * 9 / 5 + 32
                    example = f"Example: (({temp_value}K - 273.15) * 9/5) + 32 = {result}°F"

                st.success(f"✅ Result: {result} {to_unit}")
                st.info(example)

        # Length Conversion
        elif conversion_type == "Length":
            length_value = st.number_input("Enter Length Value", value=0.0)
            from_unit = st.selectbox("From Unit:", ["Meters", "Feet", "Inches", "Kilometers"])
            to_unit = st.selectbox("To Unit:", ["Meters", "Feet", "Inches", "Kilometers"])

            if st.button("Convert Length"):
                conversion_factors = {
                    "Meters": {"Feet": 3.28084, "Inches": 39.3701, "Kilometers": 0.001},
                    "Feet": {"Meters": 0.3048, "Inches": 12, "Kilometers": 0.0003048},
                    "Inches": {"Meters": 0.0254, "Feet": 0.0833333, "Kilometers": 2.54e-5},
                    "Kilometers": {"Meters": 1000, "Feet": 3280.84, "Inches": 39370.1}
                }

                if from_unit == to_unit:
                    result = length_value
                    example = f"{length_value} {from_unit} is the same as {length_value} {to_unit}."
                else:
                    result = length_value * conversion_factors[from_unit][to_unit]
                    example = f"Example: {length_value} {from_unit} * {conversion_factors[from_unit][to_unit]} = {result} {to_unit}"

                st.success(f"✅ Result: {result} {to_unit}")
                st.info(example)

    # 5. Area Calculations
    elif calculation_type == "Area Calculations":
        st.subheader("📐 Area Calculations")
        st.write("Calculate areas of geometric shapes.")

        shape = st.selectbox(
            "Select Shape:", ["Circle", "Rectangle", "Triangle"]
        )

        if shape == "Circle":
            radius = st.number_input("Enter Radius", value=1.0)
            if st.button("Calculate Area"):
                result = math.pi * radius**2
                example = f"Area = π * ({radius})^2 = {result}"
                st.success(f"✅ Area: {result}")
                st.info(example)

        elif shape == "Rectangle":
            length = st.number_input("Enter Length", value=1.0)
            width = st.number_input("Enter Width", value=1.0)
            if st.button("Calculate Area"):
                result = length * width
                example = f"Area = {length} * {width} = {result}"
                st.success(f"✅ Area: {result}")
                st.info(example)

        elif shape == "Triangle":
            base = st.number_input("Enter Base", value=1.0)
            height = st.number_input("Enter Height", value=1.0)
            if st.button("Calculate Area"):
                result = 0.5 * base * height
                example = f"Area = 0.5 * {base} * {height} = {result}"
                st.success(f"✅ Area: {result}")
                st.info(example)

    # 6. Volume Calculations
    elif calculation_type == "Volume Calculations":
        st.subheader("📦 Volume Calculations")
        st.write("Calculate volumes of geometric shapes.")

        shape = st.selectbox(
            "Select Shape:", ["Cube", "Sphere", "Cylinder"]
        )

        if shape == "Cube":
            side = st.number_input("Enter Side Length", value=1.0)
            if st.button("Calculate Volume"):
                result = side**3
                example = f"Volume = {side}^3 = {result}"
                st.success(f"✅ Volume: {result}")
                st.info(example)

        elif shape == "Sphere":
            radius = st.number_input("Enter Radius", value=1.0)
            if st.button("Calculate Volume"):
                result = (4/3) * math.pi * radius**3
                example = f"Volume = (4/3) * π * ({radius})^3 = {result}"
                st.success(f"✅ Volume: {result}")
                st.info(example)

        elif shape == "Cylinder":
            radius = st.number_input("Enter Radius", value=1.0)
            height = st.number_input("Enter Height", value=1.0)
            if st.button("Calculate Volume"):
                result = math.pi * radius**2 * height
                example = f"Volume = π * ({radius})^2 * {height} = {result}"
                st.success(f"✅ Volume: {result}")
                st.info(example)


if __name__ == "__main__":
    calculator()
