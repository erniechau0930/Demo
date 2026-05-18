import streamlit as st
import pandas as pd
import numpy as np

# ============================================
# TEXT DISPLAY FUNCTIONS
# ============================================
st.title("ISOM 3400 Final Revision - Streamlit Guide")
st.write("st.title('text') - Creates main page title")

st.header("st.header('text') - Creates section header")
st.write("st.header('text') - Creates section header")

st.subheader("st.subheader('text') - Creates subsection header")
st.write("st.subheader('text') - Creates subsection header")

st.write("st.write('text') - Generic text/data output (most flexible)")
st.write("st.write() - Can display strings, numbers, dataframes, charts, etc.")

st.markdown("st.markdown('**bold** or *italic*') - Formatted text with markdown")
st.write("st.markdown('text') - Supports **bold** with ** text **, *italic* with * text *, ~~strikethrough~~ with ~~ text ~~, bullet points with *text, etc.")

if st.button("Click me"):
    st.success("Button clicked!")
st.write("st.button('label') - Creates clickable button, returns True when clicked")

st.success("st.success('message') - Green success message box")
st.write("st.success('text') - Displays success notification in green box")

st.divider()
st.write("st.divider() - Adds horizontal line separator")

# ============================================
# FILE UPLOADER
# ============================================
st.header("st.file_uploader()")
uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])
st.write("st.file_uploader('label', type=['csv', 'txt']) - File upload widget, returns uploaded file object")

if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write(f"File uploaded: {uploaded_file.name}")
    st.dataframe(df_uploaded)
    st.write("pd.read_csv(file) - Reads CSV file into DataFrame")

st.divider()

# ============================================
# LAYOUT: TABS
# ============================================
st.header("st.tabs()")
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
st.write("st.tabs(['tab1_name', 'tab2_name', 'tab3_name']) - Creates tabbed interface, returns tab objects")

with tab1:
    st.write("Content for Tab 1")
    st.write("Use 'with tab_name:' to add content to each tab")

with tab2:
    st.write("Content for Tab 2")

with tab3:
    st.write("Content for Tab 3")

st.divider()

# ============================================
# LAYOUT: COLUMNS
# ============================================
st.header("st.columns()")
col1, col2, col3 = st.columns(3)
st.write("st.columns(number) - Creates side-by-side columns, returns column objects")

with col1:
    st.write("Column 1")
    st.button("Btn 1", key="c1")
    st.write("Use 'with col_name:' to add content")

with col2:
    st.write("Column 2")
    st.button("Btn 2", key="c2")

with col3:
    st.write("Column 3")
    st.button("Btn 3", key="c3")

st.divider()

# ============================================
# SIDEBAR
# ============================================
st.header("st.sidebar - Sidebar Navigation")
st.write("st.sidebar - Anything with st.sidebar.xxx() appears in the sidebar panel")

with st.sidebar:
    st.write("**Sidebar Content**")
    st.write("Use 'with st.sidebar:' to add widgets to sidebar")
    st.title("Sidebar Menu")
    st.write("st.sidebar.title() - Title in sidebar")
    
    sidebar_name = st.text_input("Your Name", key="sidebar_name")
    st.write("st.sidebar.text_input() - Text input in sidebar")
    
    sidebar_age = st.number_input("Your Age", min_value=0, max_value=120, value=25, key="sidebar_age")
    st.write("st.sidebar.number_input() - Number input in sidebar")
    
    sidebar_color = st.selectbox("Favorite Color", ["Red", "Blue", "Green", "Yellow"], key="sidebar_color")
    st.write("st.sidebar.selectbox() - Dropdown in sidebar")
    
    if st.sidebar.button("Sidebar Button"):
        st.sidebar.success("Button clicked in sidebar!")
    st.write("st.sidebar.button() - Button in sidebar")

st.write("st.sidebar - Great for filters, navigation, and controls that persist across pages")

st.divider()

# ============================================
# DATA DISPLAY FUNCTIONS
# ============================================
st.header("Data Display Functions")

# Create DataFrame using pd.DataFrame()
df = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Price': [999, 25, 75, 299],
    'Quantity': [10, 50, 30, 15]
})
st.write("pd.DataFrame({'col1': [values], 'col2': [values]}) - Creates DataFrame from dictionary")

st.subheader("st.dataframe()")
st.dataframe(df, use_container_width=True)
st.write("st.dataframe(dataframe, use_container_width=True) - Interactive table (sortable, resizable columns)")

st.subheader("st.table()")
st.table(df.head())
st.write("st.table(dataframe) - Static table (no sorting, no interaction)")

st.subheader("st.data_editor()")
edited_df = st.data_editor(df, num_rows="dynamic", key="editor")
st.write("st.data_editor(dataframe, num_rows='dynamic') - Editable table, users can modify cells and add/remove rows")

# df[] - accessing columns
st.subheader("df[] - Accessing columns")
st.write(df['Price'])
st.write("df['column_name'] - Accesses specific column from DataFrame")

df["Quantity"]

# df[(condition)] - filtering rows
st.subheader("df[(condition)] - Filtering rows")
st.write("Products with Price > 100:")
expensive = df[df['Price'] > 100]
st.dataframe(expensive)
st.write("df[df['column'] > value] - Filters rows where condition is True")

st.divider()

# ============================================
# INPUT WIDGETS
# ============================================
st.header("Input Widgets")

name = st.text_input("Enter your name", placeholder="Type here...")
st.write("st.text_input('label', placeholder='text', max_chars=None) - Single line text entry")

age = st.number_input("Enter your age", min_value=0, max_value=120, value=25, step=1)
st.write("st.number_input('label', min_value, max_value, value, step) - Numeric input with up/down buttons")

# st.slider - ADDED
slider_value = st.slider("Select a value", min_value=0, max_value=100, value=50, step=5)
st.write("st.slider('label', min_value, max_value, value, step) - Slider widget for selecting numeric values")

color = st.selectbox("Choose your favorite color", ["Red", "Blue", "Green", "Yellow"])
st.write("st.selectbox('label', options_list, index=0) - Dropdown selection menu")

st.write(f"**Your inputs:** Name: {name}, Age: {age}, Slider: {slider_value}, Color: {color}")

st.divider()

# ============================================
# FORM (st.form + st.form_submit_button)
# ============================================
st.header("st.form() and st.form_submit_button()")

with st.form(key="profile_form"):
    st.write("Content inside st.form() - Widgets here don't trigger reruns until submit")
    
    form_name = st.text_input("Full Name")
    form_age = st.number_input("Age", min_value=0, max_value=120)
    form_occupation = st.selectbox("Occupation", ["Student", "Engineer", "Manager"])
    
    submitted = st.form_submit_button("Submit Profile")
    st.write("st.form_submit_button('label') - Submit button for forms (different from st.button())")
    st.write("Note: st.button() cannot be used inside st.form()")

st.write("st.form(key='unique_key') - Groups widgets together, prevents reruns until submit")

if submitted:
    st.success("Form submitted!")
    st.write(f"Name: {form_name}, Age: {form_age}, Occupation: {form_occupation}")

st.divider()

# ============================================
# BAR CHART
# ============================================
st.header("st.bar_chart()")

chart_data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 12, 67]
})
st.dataframe(chart_data)
st.write("Data for chart - needs numeric column for values")

st.bar_chart(chart_data.set_index('Category'))
st.write("st.bar_chart(dataframe.set_index('x_column')) - Creates bar chart, x-axis from index, y-axis from numeric values")

# Alternative with direct data
st.bar_chart(chart_data.set_index('Category')['Values'])
st.write("st.bar_chart(df.set_index('label_column')['value_column']) - Bar chart from DataFrame column")

st.divider()

# ============================================
# OPTION MENU (requires extra package)
# ============================================
st.header("option_menu() - Navigation Menu")
st.write("option_menu(menu_title='', options=[], icons=[], default_index=0) - Creates navigation menu")
st.write("Note: Requires 'pip install streamlit-option-menu'")

try:
    from streamlit_option_menu import option_menu
    
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Data", "Charts"],
        icons=["house", "table", "bar-chart"],
        default_index=0,
    )
    
    st.write("Format: option_menu(menu_title='Title', options=list, icons=list, default_index=int, orientation='horizontal')")
    st.write(f"You selected: {selected}")
    
    if selected == "Home":
        st.write("Home page content")
    elif selected == "Data":
        st.dataframe(df)
    elif selected == "Charts":
        st.bar_chart(df.set_index('Product')['Price'])
        
except ImportError:
    st.warning("streamlit-option-menu not installed. Run: pip install streamlit-option-menu")
    st.code("""
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
# COMPLETE SUMMARY CHEAT SHEET
# ============================================
st.header("📚 Complete Function Reference")

cheat_data = {
    "Function": [
        "st.title()",
        "st.header()",
        "st.subheader()",
        "st.write()",
        "st.markdown()",
        "st.button()",
        "st.success()",
        "st.file_uploader()",
        "st.tabs()",
        "st.columns()",
        "st.sidebar",
        "st.dataframe()",
        "st.table()",
        "st.data_editor()",
        "st.text_input()",
        "st.number_input()",
        "st.slider()",
        "st.selectbox()",
        "st.form()",
        "st.form_submit_button()",
        "st.bar_chart()",
        "pd.DataFrame()",
        "pd.read_csv()",
        "df[]",
        "df[(condition)]",
        "option_menu()"
    ],
    "Format / Parameters": [
        "st.title('text')",
        "st.header('text')",
        "st.subheader('text')",
        "st.write(anything)",
        "st.markdown('**bold** *italic*')",
        "st.button('label')",
        "st.success('message')",
        "st.file_uploader('label', type=['csv'])",
        "tab1, tab2 = st.tabs(['Name1','Name2'])",
        "col1, col2 = st.columns(2)",
        "with st.sidebar: (add widgets inside)",
        "st.dataframe(df, use_container_width=True)",
        "st.table(df)",
        "st.data_editor(df, num_rows='dynamic')",
        "st.text_input('label', placeholder='text')",
        "st.number_input('label', min, max, value, step)",
        "st.slider('label', min_value, max_value, value, step)",
        "st.selectbox('label', [options])",
        "with st.form(key='name'):",
        "st.form_submit_button('label')",
        "st.bar_chart(df.set_index('x')['y'])",
        "pd.DataFrame({'col': [values]})",
        "pd.read_csv('filename.csv')",
        "df['column_name']",
        "df[df['column'] > value]",
        "option_menu(menu_title='', options=[], icons=[], default_index=0)"
    ],
    "What it does": [
        "Main page title",
        "Section header",
        "Subsection header",
        "Display anything",
        "Formatted text",
        "Clickable button",
        "Green success box",
        "Upload files",
        "Tabbed interface",
        "Side-by-side columns",
        "Sidebar panel (persistent)",
        "Interactive table (sort/resize)",
        "Static table",
        "Editable table",
        "Text entry field",
        "Number entry with arrows",
        "Slider for numeric selection",
        "Dropdown menu",
        "Groups inputs together",
        "Submit button for forms",
        "Bar chart",
        "Create DataFrame",
        "Read CSV file",
        "Access column",
        "Filter rows",
        "Navigation menu"
    ]
}

st.dataframe(pd.DataFrame(cheat_data), use_container_width=True, hide_index=True)
st.write("Each row shows: Function name → Format/Parameters → What it does")

st.success("✅ Complete! Every function shows its format on the website - no need to check GitHub!")
