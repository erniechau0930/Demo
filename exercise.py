import streamlit as st


st.title("Contact Info Collector App")
st.write("This app helps you collect Contact Info") 
st.write("Please fill in the following form:")

with st.form(key = "my_form"):
  first_name = st.text_input("Enter your first name:")
  if first_name == "":
  st.warning("The empty is empty, please enter your first name!")
  last_name = st.text_input("Enter your last name:")
  if last_name == "":s
  st.warning("The empty is empty, please enter your last name!")
  favorite_number = st.number_input("Enter your favorite number:")

  
  
  if st.form_submit_button("Register"):
    st.success(f"Registration Success,Thank you!")

