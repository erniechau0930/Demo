"import math
import streamlit as st

st.header(""Scientific Functions"")

operation_sci = st.selectbox(
    ""Choose scientific operation"", 
    [""Square Root"", ""Power"", ""Sin"", ""Cos"", ""Tan""]
)

# Dynamically change the primary label based on the operation
if operation_sci in [""Sin"", ""Cos"", ""Tan""]:
    value_label = ""Enter angle in degrees""
else:
    value_label = ""Enter base value""

value = st.number_input(value_label, value=0.0)

# Only show the second input if ""Power"" is selected
result = None
if operation_sci == ""Power"":
    exponent = st.number_input(""Enter exponent (power)"", value=2.0)
    if st.button(""Calculate""):
        result = math.pow(value, exponent)

elif operation_sci == ""Square Root"":
    if st.button(""Calculate""):
        if value < 0:
            st.error(""Cannot calculate square root of a negative number."")
        else:
            result = math.sqrt(value)

else:  # Trig functions
    if st.button(""Calculate""):
        rad = math.radians(value)
        if operation_sci == ""Sin"":
            result = math.sin(rad)
        elif operation_sci == ""Cos"":
            result = math.cos(rad)
        elif operation_sci == ""Tan"":
            result = math.tan(rad)

# Display result if one was calculated
if result is not None:
    st.success(f""The {operation_sci} result is: {result}"")"
