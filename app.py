import streamlit as st

st.set_page_config(
    page_title="Google Unit Converter",
    page_icon="🔄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("<h1 style='text-align: center; color: black;'>Google Unit Converter</h1>", unsafe_allow_html=True)

# Define unit categories and conversion factors (units in base unit equivalents)
unit_categories = {
    "Length": {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    },
    "Temperature": "Special"
}

# Select unit category
category = st.selectbox("Select a unit category:", list(unit_categories.keys()))

if category == "Temperature":
    # Temperature conversion
    temp_from = st.selectbox("Convert from:", ["Celsius", "Fahrenheit", "Kelvin"])
    temp_to = st.selectbox("Convert to:", ["Celsius", "Fahrenheit", "Kelvin"])
    temp_value = st.number_input("Enter temperature:", format="%.2f")

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32

    if st.button("Convert Temperature"):
        temp_result = convert_temperature(temp_value, temp_from, temp_to)
        st.success(f"{temp_value} {temp_from} is equal to {temp_result:.2f} {temp_to}")

else:
    # Select units
    from_unit = st.selectbox("Convert from:", list(unit_categories[category].keys()))
    to_unit = st.selectbox("Convert to:", list(unit_categories[category].keys()))

    # Get user input
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

    # Convert units
    if st.button("Convert"):
        if value == 0:
            st.warning("Please enter a value greater than 0 for conversion.")
        else:
            # Corrected formula: (from_unit / to_unit)
            result = value * (unit_categories[category][from_unit] / unit_categories[category][to_unit])
            st.success(f"{value} {from_unit} is equal to {result:.6f} {to_unit}")