import streamlit as st
import pandas as pd
import numpy as np

# ============================================
# PAGE CONFIGURATION (must be first command)
# ============================================
st.set_page_config(page_title="Streamlit Revision Guide", layout="wide")

# ============================================
# TEXT DISPLAY FUNCTIONS
# ============================================
st.title("ISOM 3400 Final Revision - Complete Streamlit Guide")
st.title("st.title() - Main page title")

st.header("st.header() - Section header")
st.subheader("st.subheader() - Subsection header")

st.write("st.write() - Generic text/anything (most flexible)")
st.markdown("st.markdown() - You can make text **bold**, *italicized*, or ~~strikethrough~~")
st.markdown("""
* Bullet points
* With st.markdown() or st.write()
""")

if st.button("st.button() - Click me!"):
    st.success("st.success() - Success message!")
    st.info("st.info() - Info message")
    st.warning("st.warning() - Warning message")
    st.error("st.error() - Error message")

st.divider()

# ============================================
# FILE UPLOADER
# ============================================
st.header("st.file_uploader() - Upload files")
uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'], help="Only CSV files")
if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write(f"Uploaded: {uploaded_file.name}")
    st.dataframe(df_uploaded.head())

st.divider()

# ============================================
# LAYOUT FUNCTIONS: TABS
# ============================================
st.header("st.tabs() - Tabbed interface")
tab1, tab2, tab3 = st.tabs(["📁 File Upload", "📊 Data Display", "⚙️ Settings"])

with tab1:
    st.write("Upload your data here")
    st.file_uploader("Choose file", key="tab_file")

with tab2:
    st.write("Preview your data")
    sample_df = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]})
    st.dataframe(sample_df)

with tab3:
    st.write("Adjust settings")
    theme = st.selectbox("Theme", ["Light", "Dark"])

st.divider()

# ============================================
# LAYOUT FUNCTIONS: COLUMNS
# ============================================
st.header("st.columns() - Side-by-side layout")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("st.metric() - Temperature", "72°F", "-2°F")
with col2:
    st.metric("Humidity", "45%", "+5%")
with col3:
    st.metric("Wind", "12 mph", "-3 mph")

# Different width columns
st.write("Columns with different widths: st.columns([2,1,1])")
colA, colB, colC = st.columns([2, 1, 1])
with colA:
    st.write("**Wider column (weight 2)**")
    st.button("Button A", key="colA")
with colB:
    st.write("**Column (weight 1)**")
    st.button("Button B", key="colB")
with colC:
    st.write("**Column (weight 1)**")
    st.button("Button C", key="colC")

st.divider()

# ============================================
# DATA DISPLAY FUNCTIONS
# ============================================
st.header("Data Display Functions")

# Create sample data
sample_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 70000, 55000],
    'Department': ['Sales', 'IT', 'Sales', 'IT']
})

# st.table() - static
st.subheader("st.table() - Static table (no interaction)")
st.table(sample_data.head(3))

# st.dataframe() - interactive
st.subheader("st.dataframe() - Interactive (click headers to sort)")
st.dataframe(sample_data, use_container_width=True)

# st.data_editor() - editable
st.subheader("st.data_editor() - Editable table")
edited_data = st.data_editor(sample_data, num_rows="dynamic", key="data_editor")
if st.button("Show edited data"):
    st.write("You edited:")
    st.dataframe(edited_data)

st.divider()

# ============================================
# CHARTS
# ============================================
st.header("Charts")

chart_data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [100, 250, 180, 300, 220],
    'Profit': [30, 80, 50, 120, 90]
})

st.subheader("st.bar_chart() - Simple bar chart")
st.bar_chart(chart_data.set_index('Category'))

st.subheader("st.line_chart() - Line chart")
st.line_chart(chart_data.set_index('Category'))

st.subheader("st.area_chart() - Area chart")
st.area_chart(chart_data.set_index('Category'))

# st.pyplot() - for matplotlib plots
st.subheader("st.pyplot() - Matplotlib plots")
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar(chart_data['Category'], chart_data['Sales'])
ax.set_title("Sales by Category")
st.pyplot(fig)

st.divider()

# ============================================
# INPUT WIDGETS
# ============================================
st.header("Input Widgets")

# Individual widgets
st.subheader("Individual Widgets (run immediately)")

# st.text_input
name = st.text_input("st.text_input() - Name", placeholder="Enter your name", max_chars=50)

# st.number_input
age = st.number_input("st.number_input() - Age", min_value=0, max_value=120, value=25, step=1)

# st.selectbox
color = st.selectbox("st.selectbox() - Favorite color", ["Red", "Blue", "Green", "Yellow"], index=0)

# st.slider
rating = st.slider("st.slider() - Rating", min_value=0, max_value=100, value=75, step=5)

# st.date_input
import datetime
date = st.date_input("st.date_input() - Date", datetime.date.today())

# st.checkbox
agree = st.checkbox("st.checkbox() - I agree to terms")

# st.radio
size = st.radio("st.radio() - Size", ["Small", "Medium", "Large"])

# st.multiselect
hobbies = st.multiselect("st.multiselect() - Hobbies", ["Reading", "Sports", "Music", "Gaming"])

st.write(f"**Your inputs:** Name: {name}, Age: {age}, Color: {color}, Rating: {rating}")

st.divider()

# ============================================
# FORM (batched inputs with submit button)
# ============================================
st.header("st.form() - Batched inputs with Submit button")
st.write("st.form_submit_button() vs st.button(): Form submit only triggers ONCE when clicked")

with st.form(key="profile_form"):
    st.write("**Fill out your profile:**")
    
    form_name = st.text_input("Full Name")
    form_age = st.number_input("Age", min_value=0, max_value=120)
    form_occupation = st.selectbox("Occupation", ["Student", "Engineer", "Manager", "Other"])
    form_experience = st.slider("Years of Experience", 0, 40, 5)
    
    submit_button = st.form_submit_button(label="Submit Profile")
    st.write("st.form_submit_button() - Must be inside st.form()")

if submit_button:
    st.success("Form submitted successfully!")
    st.write(f"**Name:** {form_name}")
    st.write(f"**Age:** {form_age}")
    st.write(f"**Occupation:** {form_occupation}")
    st.write(f"**Experience:** {form_experience} years")

st.divider()

# ============================================
# OPTION MENU (requires extra package)
# ============================================
st.header("option_menu() - Navigation Menu")
st.write("**Note:** Requires `pip install streamlit-option-menu`")

try:
    from streamlit_option_menu import option_menu
    
    selected = option_menu(
        menu_title="Navigation Menu",
        options=["Home", "Data", "Charts", "Settings"],
        icons=["house", "database", "graph-up", "gear"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )
    
    st.write(f"option_menu() format: option_menu(menu_title='Title', options=list, icons=list, default_index=int)")
    st.write(f"**Selected:** {selected}")
    
    if selected == "Home":
        st.write("Welcome to Home page")
    elif selected == "Data":
        st.dataframe(sample_data)
    elif selected == "Charts":
        st.bar_chart(chart_data.set_index('Category'))
    elif selected == "Settings":
        st.write("Settings page content")
        
except ImportError:
    st.warning("streamlit-option_menu not installed. Run: pip install streamlit-option_menu")
    st.code("""
    from streamlit_option_menu import option_menu
    
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Profile", "Settings"],
        icons=["house", "person", "gear"],
        default_index=0,
    )
    """)

st.divider()

# ============================================
# SIDEBAR
# ============================================
st.header("st.sidebar - Sidebar navigation")
st.write("Anything with st.sidebar.xxx() appears in the sidebar")

with st.sidebar:
    st.title("Sidebar Menu")
    st.write("Use st.sidebar for navigation/filters")
    
    sidebar_option = st.selectbox("Navigate", ["Home", "Data", "Charts", "Profile"])
    st.slider("Filter value", 0, 100, 50)
    
    if st.button("Sidebar Button"):
        st.info("Button clicked in sidebar!")

st.divider()

# ============================================
# SUMMARY CHEAT SHEET
# ============================================
st.header("📚 Quick Reference Cheat Sheet")

cheat_sheet = {
    "Category": [
        "Text Display", "Text Display", "Text Display",
        "Layout", "Layout",
        "Data Display", "Data Display", "Data Display", "Data Display",
        "Charts", "Charts",
        "Input", "Input", "Input", "Input", "Input", "Input", "Input",
        "Form", "File", "Sidebar", "Menu"
    ],
    "Function": [
        "st.title()", "st.header()", "st.write()",
        "st.tabs()", "st.columns()",
        "st.table()", "st.dataframe()", "st.data_editor()", "st.metric()",
        "st.bar_chart()", "st.line_chart()",
        "st.text_input()", "st.number_input()", "st.selectbox()", "st.slider()", "st.checkbox()", "st.radio()", "st.multiselect()",
        "st.form() + st.form_submit_button()", "st.file_uploader()", "st.sidebar", "option_menu()"
    ],
    "What it does": [
        "Main page title", "Section header", "Generic text/anything",
        "Tabbed interface", "Side-by-side columns",
        "Static table", "Interactive table (sort)", "Editable table", "Display KPI cards",
        "Bar chart", "Line chart",
        "Text entry", "Number entry", "Dropdown menu", "Range slider", "True/False", "Radio buttons", "Multiple selection",
        "Batch inputs with submit", "Upload files", "Sidebar content", "Navigation menu"
    ]
}

st.dataframe(pd.DataFrame(cheat_sheet), use_container_width=True, hide_index=True)

st.success("✅ Complete Streamlit Revision Guide - All functions demonstrated!")
