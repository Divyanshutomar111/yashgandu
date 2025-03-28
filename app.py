import streamlit as st
import math

def calculator():
    """
    A Streamlit app for a comprehensive calculator with various functionalities.
    Includes examples and clear explanations for each calculation type.
    """

    # --- App Styling ---
    st.markdown(
        """
        <style>
        .reportview-container {
            background: linear-gradient(135deg, #e91e63, #673ab7); /* Pink to Purple Gradient */
            color: white; /* Set default text color to white for better contrast */
        }

        .main .block-container {
          max-width: 800px;
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

        div.block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- App Content ---
    st.title("🌸 Comprehensive Calculator")
    st.markdown("A versatile calculator with a stylish pink-purple theme. Examples provided!")

    # Input Section
    st.header("⚙️ Inputs")

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
        st.subheader("➕ Basic Arithmetic")
        st.write(
            "Perform basic calculations like addition, subtraction, multiplication, and division."
        )
        st.write("Example:  Adding 5 and 3 results in 8.")

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
            st.success(f"✅ Result: {result}")

    # 2. Scientific Calculations
    elif calculation_type == "Scientific Calculations":
        st.subheader("🔬 Scientific Calculations")
        st.write(
            "Calculate square roots, exponents, logarithms, and trigonometric functions (sine, cosine, tangent)."
        )
        st.write(
            "Example: The square root of 9 is 3.  The sine of 30 degrees is approximately 0.5."
        )

        scientific_operation = st.selectbox(
            "Select Scientific Operation:",
            ["Square Root", "Exponentiation", "Logarithm", "Sine", "Cosine", "Tangent"],
        )
        num = st.number_input("Enter Number", value=1.0)

        if st.button("Calculate"):
            try:
                if scientific_operation == "Square Root":
                    result = math.sqrt(num)
                    st.write(f"Explanation: The square root of {num} is a number that, when multiplied by itself, equals {num}.")
                elif scientific_operation == "Exponentiation":
                    exponent = st.number_input("Enter Exponent", value=2.0)
                    result = num ** exponent
                    st.write(f"Explanation: {num} raised to the power of {exponent} is {num} multiplied by itself {exponent} times.")
                elif scientific_operation == "Logarithm":
                    base = st.number_input("Enter Logarithm Base (default 10)", value=10.0)
                    if num <= 0:
                        result = "Error: Number must be positive for logarithm"
                    else:
                        result = math.log(num, base)
                        st.write(f"Explanation: The logarithm (base {base}) of {num} is the exponent to which {base} must be raised to equal {num}.")
                elif scientific_operation == "Sine":
                    result = math.sin(math.radians(num))  # Convert to radians
                    st.write(f"Explanation: Sine is a trigonometric function that relates an angle of a right triangle to the ratio of the length of the opposite side to the length of the hypotenuse.")
                elif scientific_operation == "Cosine":
                    result = math.cos(math.radians(num))  # Convert to radians
                    st.write(f"Explanation: Cosine is a trigonometric function that relates an angle of a right triangle to the ratio of the length of the adjacent side to the length of the hypotenuse.")
                elif scientific_operation == "Tangent":
                    result = math.tan(math.radians(num))  # Convert to radians
                    st.write(f"Explanation: Tangent is a trigonometric function that relates an angle of a right triangle to the ratio of the length of the opposite side to the length of the adjacent side.")
                st.success(f"✅ Result: {result}")

            except Exception as e:
                st.error(f"❌ Error: {e}")

    # 3. Unit Conversions
    elif calculation_type == "Unit Conversions":
        st.subheader("📏 Unit Conversions")
        st.write("Convert between different units of measurement, like temperature, length, weight, and currency.")
        st.write("Example: Converting 25 degrees Celsius to Fahrenheit results in 77 degrees Fahrenheit.")

        conversion_type = st.selectbox(
            "Select Conversion Type:", ["Temperature", "Length", "Weight", "Currency"]
        )

        # Temperature Conversion
        if conversion_type == "Temperature":
            st.write("Convert between Celsius, Fahrenheit, and Kelvin.")
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
                st.success(f"✅ Result: {result} {to_unit}")

        # Length Conversion (Example)
        elif conversion_type == "Length":
            st.write("Convert between Meters, Feet, Inches and Kilometers.")
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
                st.success(f"✅ Result: {result} {to_unit}")

        # You can add similar blocks for Weight and Currency conversions

    # 4. Area Calculations
    elif calculation_type == "Area Calculations":
        st.subheader("📐 Area Calculations")
        st.write("Calculate the area of different shapes, such as circles, rectangles, and triangles.")
        st.write("Example:  A rectangle with a length of 5 and a width of 4 has an area of 20.")

        shape = st.selectbox(
            "Select Shape:", ["Circle", "Rectangle", "Triangle"]
        )

        if shape == "Circle":
            radius = st.number_input("Enter Radius", value=1.0)
            st.write("Explanation: The area of a circle is calculated using the formula π * radius^2")

            if st.button("Calculate Area"):
                result = math.pi * radius**2
                st.success(f"✅ Area: {result}")
        elif shape == "Rectangle":
            length = st.number_input("Enter Length", value=1.0)
            width = st.number_input("Enter Width", value=1.0)
            st.write("Explanation: The area of a rectangle is calculated by multiplying its length and width.")
            if st.button("Calculate Area"):
                result = length * width
                st.success(f"✅ Area: {result}")
        elif shape == "Triangle":
            base = st.number_input("Enter Base", value=1.0)
            height = st.number_input("Enter Height", value=1.0)
            st.write("Explanation: The area of a triangle is calculated as 0.5 * base * height.")

            if st.button("Calculate Area"):
                result = 0.5 * base * height
                st.success(f"✅ Area: {result}")

    # 5. Volume Calculations
    elif calculation_type == "Volume Calculations":
        st.subheader("📦 Volume Calculations")
        st.write("Calculate the volume of different 3D shapes like cubes, spheres, and cylinders.")
        st.write("Example: A cube with a side length of 2 has a volume of 8.")

        shape = st.selectbox(
            "Select Shape:", ["Cube", "Sphere", "Cylinder"]
        )

        if shape == "Cube":
            side = st.number_input("Enter Side Length", value=1.0)
            st.write("Explanation: The volume of a cube is calculated by cubing the side length (side * side * side).")

            if st.button("Calculate Volume"):
                result = side**3
                st.success(f"✅ Volume: {result}")
        elif shape == "Sphere":
            radius = st.number_input("Enter Radius", value=1.0)
            st.write("Explanation: The volume of a sphere is calculated using the formula (4/3) * π * radius^3.")

            if st.button("Calculate Volume"):
                result = (4/3) * math.pi * radius**3
                st.success(f"✅ Volume: {result}")
        elif shape == "Cylinder":
            radius = st.number_input("Enter Radius", value=1.0)
            height = st.number_input("Enter Height", value=1.0)
            st.write("Explanation: The volume of a cylinder is calculated using the formula π * radius^2 * height.")

            if st.button("Calculate Volume"):
                result = math.pi * radius**2 * height
                st.success(f"✅ Volume: {result}")

if __name__ == "__main__":
    calculator()
