import streamlit as st
import pandas as pd

# ============================================
# SIDEBAR - PAGE NAVIGATION
# ============================================
with st.sidebar:
    st.title("📚 Navigation")
    st.write("Use the menu below to navigate:")
    
    # Navigation options
    page = st.selectbox(
        "Go to:",
        ["🏠 Home", "📊 Data Display", "📈 Charts", "📝 Forms & Inputs", "📁 File Upload", "📚 Reference"]
    )
    st.write("st.selectbox('label', options) - Dropdown for navigation")
    st.divider()
    
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
    
    st.markdown("**You can make text bold** and *italicized* using st.markdown()")
    st.write("st.markdown('text') - Supports **bold** with ** text **, *italic* with * text *, ~~strikethrough~~ with ~~ text ~~, bullet points with * text")
    
    if st.button("Click to start"):
        st.success("Welcome to the revision guide!")
    st.write("st.button('label') - Creates clickable button")
    
    st.success("Use the sidebar on the left to navigate between topics")
    st.write("st.success('message') - Green success message box")

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
    
    st.subheader("st.line_chart()")
    st.line_chart(data=chart_data.set_index('Category')['Sales'], height=300, use_container_width=True)
    st.write("st.line_chart(data=__, height=__, use_container_width=True) - Creates line chart")
    
    st.subheader("Multiple Series Line Chart")
    st.line_chart(data=chart_data.set_index('Category'), height=400, use_container_width=True)
    st.write("st.line_chart(data=dataframe.set_index('x_column')) - Multiple columns become multiple lines")
    
    # Interactive chart with slider
    st.subheader("Interactive Chart - Adjust with Slider")
    min_value = st.slider("Minimum Sales Threshold", min_value=0, max_value=70, value=20)
    st.write("st.slider('label', min, max, value) - Slider for numeric input")
    
    filtered_data = chart_data[chart_data['Sales'] >= min_value]
    st.line_chart(data=filtered_data.set_index('Category')['Sales'], height=300, use_container_width=True)
    st.write(f"Showing products with Sales >= {min_value}")

# ============================================
# FORMS & INPUTS PAGE
# ============================================

elif page == "📝 Forms & Inputs":
    st.header("Input Widgets")
    
    col1, col2 = st.columns(2)
    st.write("st.columns(number) - Creates side-by-side columns")
    
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
    st.write("st.file_uploader('label', type=['csv']) - File upload widget")
    
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
        st.write("👈 Upload a CSV file to see preview")

# ============================================
# REFERENCE PAGE
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
            "st.line_chart()",
            "st.expander()",
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
            "with st.sidebar:",
            "st.dataframe(df, use_container_width=True)",
            "st.table(df)",
            "st.data_editor(df, num_rows='dynamic')",
            "st.text_input('label', placeholder='text')",
            "st.number_input('label', min, max, value, step)",
            "st.slider('label', min, max, value, step)",
            "st.selectbox('label', [options])",
            "with st.form(key='name'):",
            "st.form_submit_button('label')",
            "st.line_chart(data=df, height=300, use_container_width=True)",
            "with st.expander('label'):",
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
            "Formatted text with **bold** and *italic*",
            "Clickable button",
            "Green success box",
            "Upload CSV files",
            "Tabbed interface",
            "Side-by-side columns",
            "Sidebar panel",
            "Interactive table (sort/resize)",
            "Static table",
            "Editable table",
            "Text entry field",
            "Number entry with arrows",
            "Slider for numeric selection",
            "Dropdown menu",
            "Groups inputs together",
            "Submit button for forms",
            "Line chart visualization",
            "Expandable section (hide/show content)",
            "Create DataFrame from dictionary",
            "Read CSV file into DataFrame",
            "Access specific column",
            "Filter rows by condition",
            "Navigation menu (requires extra package)"
        ]
    }
    
    st.dataframe(pd.DataFrame(cheat_data), use_container_width=True, hide_index=True)
    st.write("Each row shows: Function → Format → What it does")
    
    st.success("✅ Complete reference - bookmark this page!")

# ============================================
# TABS DEMO
# ============================================

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

# ============================================
# EXPANDER DEMO
# ============================================

st.divider()
st.header("st.expander() - Expandable Section")
st.write("st.expander('label') - Creates expandable section that hides/shows content")

with st.expander("Click to expand this section"):
    st.write("This content is hidden until you click the expander!")
    st.write("You can put any widgets or content inside an expander.")
    st.success("Great for organizing long pages!")

with st.expander("Another expander example"):
    st.dataframe(pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]}))

# ============================================
# COLUMNS DEMO
# ============================================

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

# ============================================
# OPTION MENU DEMO
# ============================================

st.divider()
st.header("option_menu() - Navigation Menu")
st.write("option_menu(menu_title='', options=[], icons=[], default_index=0) - Creates navigation menu")
st.write("Note: Requires 'pip install streamlit-option-menu'")

try:
    from streamlit_option_menu import option_menu
    
    selected = option_menu(
        menu_title="Demo Menu",
        options=["Home", "Data", "Charts"],
        icons=["house", "table", "bar-chart"],
        default_index=0,
        orientation="horizontal"
    )
    
    st.write(f"option_menu() format: option_menu(menu_title='Title', options=list, icons=list, default_index=int)")
    st.write(f"You selected: {selected}")
        
except ImportError:
    st.write("streamlit-option-menu not installed. Run: pip install streamlit-option-menu")
    st.write("""
    python
    from streamlit_option_menu import option_menu 
    """
    
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Data", "Charts"],
        icons=["house", "table", "bar-chart"],
        default_index=0,
    )
