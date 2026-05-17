import streamlit as st
import pandas as pd
import numpy as np

st.title("Isom 3400 Final Revision")
st.title("This is st.title()")
st.header("This is st.header()")
st.subheader("This is st.subheader()")
st.write("This is st.write()")
st.markdown("This is st.markdown() You can make text **bold** with ""** text **"", *italicized* with ""* text *"", or ~~strikethrough~~ with ""~~ text ~~"".")
st.markdown("""
* Item 1: Bullet point is made with *
* Item 2: This can be done with st.markdown(), or st.write()
""")
if st.button("This is st.button()"):
  st.success("This is st.success()")
  
with st.form(key="user_profile_form"):
    st.write("This box is created with st.form(key=xxx), need unique key value inside st.form()")
    
    name = st.text_input("Name", value="e.g. Jane Doe")
    st.write("format: st.text_input(label, default value)")
    
    age = st.number_input("Age", min_value=1, max_value=120, value=25, step =1)
    st.write("format: st.number_input(label, min_value, max_value, default value, step)")
    
    occupation = st.selectbox(
        "Current Occupation",
        options=["Software Engineer", "Data Scientist", "Student", "Other"]
    )
    st.write("format: st.selectbox(label, options), options is a list")
    
    submit_button = st.form_submit_button(label="Submit Profile")
    st.write("st.form_submit_button() is not the same as st.button()")

if submit_button:
    st.success(f"Form submitted successfully!")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Occupation:** {occupation}")
st.button(1)


"""st.file_uploader()
st.tabs()
st.columns()
st.table()
st.data_editor()
st.dataframe()
st.bar_chart()
st.form_submit_button()
option_menu(menu_title= “”, options= [], icons=[], default_index=0)"""
