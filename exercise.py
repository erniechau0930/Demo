import streamlit as st


st.title("Streamlit Exercise")

with st.form(key = "my_form"):
  first_name = st.text_input("Enter your first name:")
  last_name = st.text_input("Enter your last name:")
  submitted = st.form_submit_button("Submit")
  if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")
