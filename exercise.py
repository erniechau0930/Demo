import streamlit as st


st.title("Streamlit Exercise")

with st.form(key = "my_form"):
  first_name = st.text_input("Enter your first name:")
  last_name = st.text_input("Enter your last name:")
  favorite_number = st.number_inout("Enter your favorite number:")
  submitted = st.form_submit_button("Register")
  if submitted:
        st.success

