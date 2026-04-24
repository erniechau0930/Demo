import streamlit as st
# Title and Header
st.title("**Retail Business Dashboard**")
st.header("**Manager Input Selection**")

# Instruction
st.write("Please enter the monthly sales target and select the rehgion")

# Number input for sales target
st.number_input()
value = st.number_input("Enter monthly sales target (in USD):",
                      min_value=0,
                      max_value=50000,
                      value=50000)
st.write(f"Your monthly sales target is {value}")

# Dropdown for region selection
st.selectbox()
option = st.selectbox("Select region:",
                      ["North", "East", "South", "West"])
st.write(f"You selected: {option}")


# Submit button
if st.button("Submit"):
    # Display entered values



    # Success message
    st.success("Operation completed successfully!")


    # Extra message for ambitious target
