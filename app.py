import streamlit as st

st.title("Welcome to Streamlit!")

st.write("**Bottlers FC** and *Haaland*")

st.header("Section 1: Introduction")

age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)
st.write(f"Your age is {age}")

option = st.selectbox("Choose your favorite color:",
                      ["Red", "Blue", "Green"])
st.write(f"You selected: {option}")

if st.button("Click Me"):
    st.write("Button clicked!")
else
    st.write("Button not clicked!")

