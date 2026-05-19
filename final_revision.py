import streamlit as st
import pandas as pd
import numpy as np

# ============================================
# SIDEBAR - PAGE NAVIGATION
# ============================================
with st.sidebar:
    st.title("📚 Navigation")
    st.write("Use the menu below to navigate:")
    
    # Navigation options
    page = st.radio(
        "Go to:",
        ["🏠 Home", "📊 Data Display", "📈 Charts", "📝 Forms & Inputs", "📁 File Upload", "📚 Reference"]
    )
    st.write("st.radio('label', options) - Radio buttons for navigation")
    st.divider()
    
    # Quick filters (only show on relevant pages)
    st.write("**Quick Filters**")
    show_demo = st.checkbox("Show all examples", value=True)
    st.write("st.checkbox('label') - Checkbox for boolean selection")
    
    st.divider()
    st.caption("ISOM 3400 Final Revision")
    st.caption("Streamlit Guide v1.0")

st.write("st.sidebar - Sidebar panel for navigation and persistent controls")

st.divider()

# ============================================
# TEXT DISPLAY FUNCTIONS
# ============================================

if page == "🏠 Home":
    st.title("ISOM 3400 Final Revision - Streamlit Guide")
    st.write("st.title('text') - Creates main page title")
    
    st.header("Welcome to the Streamlit Guide")
    st.write("st.header('text') - Creates section header")
    
    st.subheader("Use the sidebar to navigate")
    st.write("st.subheader('text') - Creates subsection header")
    
    st.write("This guide demonstrates all Streamlit functions you need for the final exam.")
    st.write("st.write() - Generic text/data output (most flexible)")
    st.wrtie(anything you want)
    
    st.markdown("**You can make text bold** and *italicized* using st.markdown()")
    st.write("st.markdown('text') - Supports **bold** with ** text **, *italic* with * text *, ~~strikethrough~~ with ~~ text ~~, bullet points with * text")
    
    if st.button("Click to start"):
        st.success("Welcome to the revision guide!")
    st.write("st.button('label') - Creates clickable button")
    
    st.success("Use the sidebar on the left to navigate between topics")
    st.write("st.success('message') - Green success message box")

    st.markdown("**Reminder**: np.random.rnadint(min,max, size = x)")

# ============================================
# DATA DISPLAY PAGE
# ============================================

elif page == "📊 Data Display":
    st.header("Data Display Functions")
    st.write("st.header('text') - Section header")
    
    # Create DataFrame using pd.DataFrame()
    df = pd.DataFrame({
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
        'Price': [999, 25, 75, 299],
        'Quantity': [10, 50, 30, 15]
    })
    st.write("pd.DataFrame({'col1': [values], 'col2': [values]}) - Creates DataFrame from dictionary")
    
    st.subheader("st.dataframe() - Interactive Table")
    st.dataframe(df, use_container_width=True)
    st.write("st.dataframe(dataframe, use_container_width=True) - Sortable, resizable columns")
    
    st.subheader("st.table() - Static Table")
    st.table(df.head())
    st.write("st.table(dataframe) - Static table, no interaction")
    
    st.subheader("st.data_editor() - Editable Table")
    edited_df = st.data_editor(df, num_rows="dynamic", key="editor")
    st.write("st.data_editor(dataframe, num_rows='dynamic') - Users can edit cells")
    
    # df[] - accessing columns
    st.subheader("df[] - Accessing Columns")
    st.write(df['Price'])
    st.write("df['column_name'] - Accesses specific column")
    
    # df[(condition)] - filtering rows
    st.subheader("df[(condition)] - Filtering Rows")
    st.write("Products with Price > 100:")
    expensive = df[df['Price'] > 100]
    st.dataframe(expensive)
    st.write("df[df['column'] > value] - Filters rows where condition is True")

# ============================================
# CHARTS PAGE
# ============================================

elif page == "📈 Charts":
    st.header("Chart Functions")
    
    chart_data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Sales': [23, 45, 12, 67, 34],
        'Profit': [10, 25, 5, 40, 20]
    })
    st.write("Sample Data for Charts:")
    st.dataframe(chart_data)
    
    st.subheader("st.bar_chart()")
    st.bar_chart(chart_data.set_index('Category')['Sales'])
    st.write("st.bar_chart(dataframe.set_index('x_column')['y_column']) - Creates bar chart")
    
    st.subheader("Multiple Series Bar Chart")
    st.bar_chart(chart_data.set_index('Category'))
    st.write("st.bar_chart(dataframe.set_index('x_column')) - Multiple columns become multiple bars")
    
    # Interactive chart with slider
    st.subheader("Interactive Chart - Adjust with Slider")
    min_value = st.slider("Minimum Sales Threshold", min_value=0, max_value=70, value=20)
    st.write("st.slider('label', min, max, value) - Slider for numeric input")
    
    filtered_data = chart_data[chart_data['Sales'] >= min_value]
    st.bar_chart(filtered_data.set_index('Category')['Sales'])
    st.write(f"Showing products with Sales >= {min_value}")

# ============================================
# FORMS & INPUTS PAGE
# ============================================

elif page == "📝 Forms & Inputs":
    st.header("Input Widgets")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Individual Widgets")
        name = st.text_input("Enter your name", placeholder="Type here...")
        st.write("st.text_input('label', placeholder='text')")
        
        age = st.number_input("Enter your age", min_value=0, max_value=120, value=25, step=1)
        st.write("st.number_input('label', min, max, value, step)")
        
        rating = st.slider("Rate your experience", min_value=0, max_value=10, value=5, step=1)
        st.write("st.slider('label', min, max, value, step)")
        
        color = st.selectbox("Choose favorite color", ["Red", "Blue", "Green", "Yellow"])
        st.write("st.selectbox('label', [options])")
    
    with col2:
        st.subheader("Your Selections")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Rating:** {rating}/10")
        st.write(f"**Color:** {color}")
    
    st.divider()
    
    st.header("st.form() - Submit Button Pattern")
    st.write("Use forms when you want all data submitted at once (not on every change)")
    
    with st.form(key="profile_form"):
        st.write("**Registration Form**")
        
        form_name = st.text_input("Full Name")
        form_email = st.text_input("Email")
        form_age = st.number_input("Age", min_value=0, max_value=120)
        form_occupation = st.selectbox("Occupation", ["Student", "Engineer", "Manager", "Other"])
        
        submitted = st.form_submit_button("Register")
        st.write("st.form_submit_button('label') - Only triggers when clicked")
    
    if submitted:
        st.success(f"Welcome {form_name}! Registration complete.")
        st.write(f"Email: {form_email}, Age: {form_age}, Occupation: {form_occupation}")

# ============================================
# FILE UPLOAD PAGE
# ============================================

elif page == "📁 File Upload":
    st.header("st.file_uploader() - Upload CSV Files")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
    st.write("st.file_uploader('label', type=['csv', 'txt']) - File upload widget")
    
    if uploaded_file is not None:
        df_uploaded = pd.read_csv(uploaded_file)
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        st.write("pd.read_csv(file) - Reads CSV into DataFrame")
        
        st.subheader("File Preview")
        st.dataframe(df_uploaded)
        
        st.subheader("File Info")
        st.write(f"**Rows:** {df_uploaded.shape[0]}")
        st.write(f"**Columns:** {df_uploaded.shape[1]}")
        st.write(f"**Column Names:** {list(df_uploaded.columns)}")
    else:
        st.info("👈 Upload a CSV file to see preview")
        st.write("st.info('message') - Blue info box")

# ============================================
# REFERENCE PAGE (was COMPLETE SUMMARY CHEAT SHEET)
# ============================================

elif page == "📚 Reference":
    st.header("Complete Function Reference")
    
    cheat_data = {
        "Function": [
            "st.title()",
            "st.header()",
            "st.subheader()",
            "st.write()",
            "st.markdown()",
            "st.button()",
            "st.success()",
            "st.info()",
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
            "st.radio()",
            "st.checkbox()",
            "st.form()",
            "st.form_submit_button()",
            "st.bar_chart()",
            "pd.DataFrame()",
            "pd.read_csv()",
            "df[]",
            "df[(condition)]"
        ],
        "Format / Parameters": [
            "st.title('text')",
            "st.header('text')",
            "st.subheader('text')",
            "st.write(anything)",
            "st.markdown('**bold**')",
            "st.button('label')",
            "st.success('message')",
            "st.info('message')",
            "st.file_uploader('label', type=['csv'])",
            "tab1, tab2 = st.tabs(['A','B'])",
            "col1, col2 = st.columns(2)",
            "with st.sidebar:",
            "st.dataframe(df, use_container_width=True)",
            "st.table(df)",
            "st.data_editor(df, num_rows='dynamic')",
            "st.text_input('label', placeholder='text')",
            "st.number_input('label', min, max, value, step)",
            "st.slider('label', min, max, value, step)",
            "st.selectbox('label', [options])",
            "st.radio('label', [options])",
            "st.checkbox('label')",
            "with st.form(key='name'):",
            "st.form_submit_button('label')",
            "st.bar_chart(df.set_index('x')['y'])",
            "pd.DataFrame({'col': [values]})",
            "pd.read_csv('filename.csv')",
            "df['column_name']",
            "df[df['column'] > value]"
        ],
        "What it does": [
            "Main title", "Section header", "Subsection header",
            "Display anything", "Formatted text", "Clickable button",
            "Green success box", "Blue info box", "Upload files",
            "Tabbed interface", "Side-by-side columns", "Sidebar panel",
            "Interactive table", "Static table", "Editable table",
            "Text entry", "Number entry", "Slider selection",
            "Dropdown menu", "Radio buttons", "Checkbox",
            "Groups inputs", "Submit button", "Bar chart",
            "Create DataFrame", "Read CSV", "Access column", "Filter rows"
        ]
    }
    
    st.dataframe(pd.DataFrame(cheat_data), use_container_width=True, hide_index=True)
    st.write("Each row shows: Function → Format → What it does")
    
    st.success("✅ Complete reference - bookmark this page!")

# ============================================
# TABS DEMO (only shown if show_demo is True)
# ============================================

if show_demo and page != "📚 Reference":
    st.divider()
    st.header("st.tabs() - Tabbed Interface Demo")
    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
    st.write("st.tabs(['tab1_name', 'tab2_name', 'tab3_name']) - Creates tabs")
    
    with tab1:
        st.write("Content for Tab 1")
    with tab2:
        st.write("Content for Tab 2")
    with tab3:
        st.write("Content for Tab 3")
    
    st.divider()
    st.header("st.columns() - Column Layout Demo")
    col1, col2, col3 = st.columns(3)
    st.write("st.columns(number) - Creates columns")
    
    with col1:
        st.write("Column 1")
    with col2:
        st.write("Column 2")
    with col3:
        st.write("Column 3")
