import streamlit as st


st.title("Streamlit Exercise")

with st.form(key = "my_form"):
  first_name = st.text_input("Enter your first name:")
  last_name = st.text_input("Enter your last name:")
