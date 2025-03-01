import streamlit as st

# Conversion dictionary
CONVERSION_FACTORS = {
    "Meters": 1,
    "Kilometers": 0.001,
    "Centimeters": 100,
    "Miles": 0.000621371,
    "Feet": 3.28084,
    "Inches": 39.3701,
    "Yards": 1.09361
}

# Conversion function
def convert_units(value, from_unit, to_unit):
    if from_unit not in CONVERSION_FACTORS or to_unit not in CONVERSION_FACTORS:
        return "Invalid unit"
    
    value_in_meters = value / CONVERSION_FACTORS[from_unit]  # Convert to meters first
    return round(value_in_meters * CONVERSION_FACTORS[to_unit], 4)  # Convert to target unit

# Streamlit UI
st.title("🔄 Unit Converter")

st.markdown("Convert between different length units easily!")

# User input
value = st.number_input("Enter value:", min_value=0.0, format="%.2f", step=0.1)

# Unit selection
units = list(CONVERSION_FACTORS.keys())
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("Convert from:", units)
with col2:
    to_unit = st.selectbox("Convert to:", units)

# Live conversion result
if value > 0:
    result = convert_units(value, from_unit, to_unit)
    st.success(f"✅ {value:.2f} {from_unit} = **{result} {to_unit}**")
# Convert Button
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"✅ Converted Value: {result} {to_unit}")

# Reset button
if st.button("Reset 🔄"):
    st.experimental_rerun()
