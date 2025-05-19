import streamlit as st

st.title("🔁 Simple Unit Converter")

units = {
    "Meter": 1,
    "Kilometer": 1000,
    "Foot": 0.3048,
    "Mile": 1609.34
}

# User inputs
from_unit = st.selectbox("From Unit", list(units.keys()))
to_unit = st.selectbox("To Unit", list(units.keys()))
value = st.number_input("Enter Value", min_value=0.0)

# Conversion
if st.button("Convert"):
    value_in_meters = value * units[from_unit]
    converted_value = value_in_meters / units[to_unit]
    st.success(f"{value} {from_unit} = {converted_value:.4f} {to_unit}")
