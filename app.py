import streamlit as st
# Title and Header
st.title("**Retail Business Dashboard**")
st.header("**Manager Input Selection**")

# Instruction
st.write("Please enter the monthly sales target and select the region")

# Number input for sales target
sales_target = st.number_input("Enter monthly sales target (in USD):",
                      min_value=0,
                      max_value=50000,
                      value=50000)
st.write(f"Your monthly sales target is {sales_target}")

# Dropdown for region selection
region = st.selectbox("Select region:",
                      ["North", "East", "South", "West"])
st.write(f"You selected: {region}")


# Submit button
if st.button("Submit"):
    # Display entered values
    st.write(f"Your monthly sales target is {value}")
    st.write(f"You selected: {region}")


    # Success message
    st.success("Dashboard Updated successfully!")


    # Extra message for ambitious target
if sales_target > 100000:
        st.write(""Great! You have set an ambitious target!"")
