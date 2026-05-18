import streamlit as st
import pandas as pd
import numpy as np

# ============================================
# TEXT DISPLAY FUNCTIONS
# ============================================
st.title("ISOM 3400 Final Revision - Streamlit Guide")
st.title("st.title() - Main page title")

st.header("st.header() - Section header")
st.subheader("st.subheader() - Subsection header")

st.write("st.write() - Generic text (most flexible)")
st.markdown("st.markdown() - You can make text **bold**, *italicized*, or ~~strikethrough~~")
st.markdown("""
* Bullet points with st.markdown()
* Second bullet point
""")

if st.button("st.button() - Click me!"):
    st.success("st.success() - Success message!")

st.divider()

# ============================================
# FILE UPLOADER
# ============================================
st.header("st.file_uploader() - Upload CSV files")

uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])

if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write(f"File uploaded: {uploaded_file.name}")
    st.dataframe(df_uploaded.head())
    
    # Using df[] to access columns
    st.write("**First column data:**")
    first_column = df_uploaded.columns[0]
    st.write(df_uploaded[first_column])
    
    # Using df[(condition)] to filter rows
    st.write("**Filtered data (first column > 0):**")
    st.dataframe(df_uploaded[df_uploaded[first_column] > 0])

st.divider()

# ============================================
# LAYOUT: TABS
# ============================================
st.header("st.tabs() - Tabbed interface")

tab1, tab2, tab3 = st.tabs(["Data Entry", "Data Display", "Charts"])

with tab1:
    st.write("Enter your data here")
    st.text_input("Name", key="tab_name")
    st.number_input("Age", key="tab_age")

with tab2:
    st.write("Preview your data")
    sample_data = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [85, 92, 78]
    })
    st.dataframe(sample_data)

with tab3:
    st.write("Charts will appear here")

st.divider()

# ============================================
# LAYOUT: COLUMNS
# ============================================
st.header("st.columns() - Side-by-side layout")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Column 1**")
    st.button("Button 1", key="col1_btn")

with col2:
    st.write("**Column 2**")
    st.button("Button 2", key="col2_btn")

with col3:
    st.write("**Column 3**")
    st.button("Button 3", key="col3_btn")

# Columns with different widths
st.write("Columns with different widths [2,1,1]:")
colA, colB, colC = st.columns([2, 1, 1])

with colA:
    st.write("**Wider column (weight 2)**")
    st.selectbox("Option", ["A", "B", "C"], key="wide_select")

with colB:
    st.write("**Column (weight 1)**")
    st.text_input("Name", key="colB_input")

with colC:
    st.write("**Column (weight 1)**")
    st.number_input("Age", key="colC_num")

st.divider()

# ============================================
# DATA DISPLAY FUNCTIONS
# ============================================
st.header("Data Display Functions")

# Create DataFrame using pd.DataFrame()
df = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones'],
    'Price': [999, 25, 75, 299, 149],
    'Quantity': [10, 50, 30, 15, 40],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories']
})

st.subheader("Original Data - st.dataframe() (interactive)")
st.dataframe(df, use_container_width=True)
st.write("✅ Click column headers to sort | Drag edges to resize")

st.subheader("Static Table - st.table() (no interaction)")
st.table(df.head(3))

st.subheader("Editable Table - st.data_editor()")
edited_df = st.data_editor(df, num_rows="dynamic", key="data_editor")

if st.button("Show edited data"):
    st.write("You edited:")
    st.dataframe(edited_df)

# Using df[] to access columns
st.subheader("Accessing columns with df[]")
st.write("**Prices column:**")
st.write(df['Price'])

st.write("**Products and Prices:**")
for i in range(len(df)):
    st.write(f"{df['Product'][i]}: ${df['Price'][i]}")

# Using df[(condition)] to filter rows
st.subheader("Filtering rows with df[(condition)]")

st.write("**Products with price > $100:**")
expensive = df[df['Price'] > 100]
st.dataframe(expensive)

st.write("**Accessories category only:**")
accessories = df[df['Category'] == 'Accessories']
st.dataframe(accessories)

st.write("**Products with quantity >= 30:**")
high_stock = df[df['Quantity'] >= 30]
st.dataframe(high_stock)

st.write("**Multiple conditions (Price > 100 AND Category = Electronics):**")
electronics_expensive = df[(df['Price'] > 100) & (df['Category'] == 'Electronics')]
st.dataframe(electronics_expensive)

st.divider()

# ============================================
# INPUT WIDGETS
# ============================================
st.header("Input Widgets")

# st.text_input
name = st.text_input("st.text_input() - Enter your name", placeholder="Type here...")

# st.number_input
age = st.number_input("st.number_input() - Enter your age", min_value=0, max_value=120, value=25, step=1)

# st.selectbox
color = st.selectbox("st.selectbox() - Choose your favorite color", ["Red", "Blue", "Green", "Yellow"])

st.write(f"**Your inputs:** Name: {name}, Age: {age}, Color: {color}")

st.divider()

# ============================================
# FORM (with st.form and st.form_submit_button)
# ============================================
st.header("st.form() - Form with Submit Button")

with st.form(key="user_form"):
    st.write("**Fill out your profile:**")
    
    form_name = st.text_input("Full Name")
    form_age = st.number_input("Age", min_value=0, max_value=120)
    form_occupation = st.selectbox("Occupation", ["Student", "Engineer", "Manager", "Other"])
    form_city = st.text_input("City")
    
    submitted = st.form_submit_button("Submit Profile")
    st.write("st.form_submit_button() - Only triggers when clicked (not on every change)")

if submitted:
    st.success(f"Form submitted successfully!")
    st.write(f"**Name:** {form_name}")
    st.write(f"**Age:** {form_age}")
    st.write(f"**Occupation:** {form_occupation}")
    st.write(f"**City:** {form_city}")

st.divider()

# ============================================
# BAR CHART
# ============================================
st.header("st.bar_chart() - Bar Chart Visualization")

# Create data for chart using pd.DataFrame()
chart_data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [23, 45, 12, 67, 34]
})

st.write("**Sample Data for Chart:**")
st.dataframe(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data.set_index('Category'))

# Another example using actual data
st.subheader("Sales by Product (from our data)")
sales_by_product = df.set_index('Product')['Price']
st.bar_chart(sales_by_product)

st.divider()

# ============================================
# OPTION MENU (requires extra package)
# ============================================
st.header("option_menu() - Navigation Menu")
st.write("**Note:** Requires `pip install streamlit-option-menu`")

try:
    from streamlit_option_menu import option_menu
    
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Data", "Charts", "Profile"],
        icons=["house", "table", "bar-chart", "person"],
        default_index=0,
    )
    
    st.write(f"option_menu() format: option_menu(menu_title='Title', options=list, icons=list, default_index=int)")
    st.write(f"**You selected:** {selected}")
    
    if selected == "Home":
        st.write("Welcome to the Home page!")
    elif selected == "Data":
        st.dataframe(df)
    elif selected == "Charts":
        st.bar_chart(df.set_index('Product')['Price'])
    elif selected == "Profile":
        st.text_input("Name")
        st.number_input("Age")
        
except ImportError:
    st.warning("streamlit-option-menu not installed. Run: pip install streamlit-option-menu")
    st.code("""
    # To install:
    pip install streamlit-option-menu
    
    # Then use:
    from streamlit_option_menu import option_menu
    
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Data", "Charts"],
        icons=["house", "table", "bar-chart"],
        default_index=0,
    )
    """)

st.divider()

# ============================================
# COMPLETE EXAMPLE: Data Analysis Dashboard
# ============================================
st.header("Complete Example: Data Analysis Dashboard")

# Create data using pd.DataFrame()
sales_data = pd.DataFrame({
    'Date': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [1200, 1500, 1800, 1700, 2100, 2500],
    'Region': ['North', 'South', 'North', 'East', 'West', 'North']
})

st.subheader("Sales Data")
st.dataframe(sales_data)

# Using df[] to access column
st.subheader("Sales Column Only")
st.write(sales_data['Sales'])

# Using df[(condition)] to filter rows
st.subheader("Filter: North Region Sales Only")
north_sales = sales_data[sales_data['Region'] == 'North']
st.dataframe(north_sales)

# Bar chart of sales
st.subheader("Sales Bar Chart")
st.bar_chart(sales_data.set_index('Date')['Sales'])

# Form to add new sales data
with st.form(key="add_sales_form"):
    st.write("**Add New Sales Record:**")
    new_date = st.text_input("Month")
    new_sales = st.number_input("Sales Amount", min_value=0)
    new_region = st.selectbox("Region", ["North", "South", "East", "West"])
    
    add_submitted = st.form_submit_button("Add Record")
    
    if add_submitted:
        st.success(f"Added: {new_date} - ${new_sales} ({new_region})")

st.divider()

# ============================================
# SUMMARY CHEAT SHEET
# ============================================
st.header("📚 Quick Reference - All Functions Used")

st.write("""
**Streamlit Functions:**
- `st.title()` - Main title
- `st.header()` - Section header  
- `st.subheader()` - Subsection header
- `st.write()` - Generic text/data output
- `st.markdown()` - Formatted text with markdown
- `st.button()` - Clickable button
- `st.success()` - Success message
- `st.file_uploader()` - Upload CSV files
- `st.tabs()` - Tabbed interface
- `st.columns()` - Side-by-side layout
- `st.dataframe()` - Interactive table
- `st.table()` - Static table
- `st.data_editor()` - Editable table
- `st.text_input()` - Text entry field
- `st.number_input()` - Number entry field
- `st.selectbox()` - Dropdown menu
- `st.form()` - Group inputs together
- `st.form_submit_button()` - Submit button for forms
- `st.bar_chart()` - Bar chart visualization
- `option_menu()` - Navigation menu (extra package)

**Pandas Functions:**
- `pd.DataFrame()` - Create DataFrame from data
- `pd.read_csv()` - Read CSV file into DataFrame
- `df[]` - Access specific column
- `df[(condition)]` - Filter rows by condition
""")

st.success("✅ Complete! All functions from your list are demonstrated above.")
