import streamlit as st
import pandas as pd
import numpy as np

st.title("Isom 3400 Final Revision")
st.header("Exam Date: 21st May, 12:30pm")
st.subheader("Location: LTA")
st.title("This is st.title")
st.header("This is st.header")
st.subheader("This is st.subheader")
st.write("This is st.write")
st.markdown("This is st.markdown You can make text **bold** with ""** text **"", *italicized* with ""* text *"", or ~~strikethrough~~ with ""~~ text ~~"".")
st.markdown("""
* Item 1: Bullet point is made with *
* Item 2: This can be done with st.markdown, or st.write
""")
if st.button("This is st.button"):
  st.success("This is st.success")
  

st.text_input("This is text input")



"""st.file_uploader()
st.tabs()
st.columns()
st.table()
st.data_editor()
st.dataframe()
st.selectbox()
st.text_input()
st.number_input()
st.form()
st.bar_chart()
st.form_submit_button()
option_menu(menu_title= “”, options= [], icons=[], default_index=0)"""
