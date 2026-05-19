import streamlit as st
import pandas as pd

# ============================================
# SIDEBAR - PAGE NAVIGATION
# ============================================
st.sidebar.title("Navigation")     # ✅ Title in sidebar
st.sidebar.write("Content here")   # ✅ Write in sidebar
st.sidebar.selectbox("Options", ["A","B"])  # ✅ Selectbox in sidebar

with st.sidebar:
    st.title("📚 Navigation")
    st.write("st.sidebar.title() - Title in sidebar")
    st.write("Use the menu below to navigate:")
    st.write("st.sidebar.write() - Text in sidebar")
    
    # Navigation options
    page = st.radio(
        "Go to:",
        ["🏠 Home", "📊 Data Display", "📈 Charts", "📚 Reference"]
    )
    st.write("st.sidebar.radio() - Radio buttons for navigation")

st.divider()

# ============================================
# TEXT DISPLAY FUNCTIONS - HOME PAGE
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
    st.table(df)
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
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Sales': [100, 200, 150, 300, 250],
        'Profit': [30, 50, 40, 80, 70]
    })
    st.write("Sample Data for Charts:")
    st.dataframe(chart_data)
    
    st.subheader("st.line_chart() - Single Series")
    st.line_chart(data=chart_data.set_index('Month')['Sales'], height=300, use_container_width=True)
    st.write("st.line_chart(data=df.set_index('x')['y'], height=300, use_container_width=True)")
    
    st.subheader("st.line_chart() - Multiple Series")
    st.line_chart(data=chart_data.set_index('Month'), height=400, use_container_width=True)
    st.write("st.line_chart(data=df.set_index('x'), height=400, use_container_width=True) - Multiple columns become multiple lines")

# ============================================
# REFERENCE PAGE
# ============================================

elif page == "📚 Reference":
    st.header("Complete Function Reference - Tested Methods Only")
    
    cheat_data = {
        "Function": [
            "st.title()",
            "st.header()",
            "st.subheader()",
            "st.write()",
            "st.markdown()",
            "st.success()",
            "st.sidebar",
            "st.tabs()",
            "st.columns()",
            "st.dataframe()",
            "st.table()",
            "st.data_editor()",
            "st.line_chart()",
            "st.expander()",
            "pd.DataFrame()",
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
            "st.success('message')",
            "with st.sidebar:",
            "tab1, tab2 = st.tabs(['A','B'])",
            "col1, col2 = st.columns(2)",
            "st.dataframe(df, use_container_width=True)",
            "st.table(df)",
            "st.data_editor(df, num_rows='dynamic')",
            "st.line_chart(data=df, height=300, use_container_width=True)",
            "with st.expander('label'):",
            "pd.DataFrame({'col': [values]})",
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
            "Green success message box",
            "Sidebar panel for navigation",
            "Tabbed interface",
            "Side-by-side columns",
            "Interactive table (sortable, resizable)",
            "Static table (no interaction)",
            "Editable table (users can modify cells)",
            "Line chart visualization",
            "Expandable section (hide/show content)",
            "Create DataFrame from dictionary",
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
st.write("st.tabs(['tab1_name', 'tab2_name', 'tab3_name']) - Creates tabs")

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Content for Tab 1")
    st.write("Use 'with tab_name:' to add content to each tab")

with tab2:
    st.write("Content for Tab 2")
    st.dataframe(pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]}))

with tab3:
    st.write("Content for Tab 3")
    st.success("You can put any content inside tabs!")

# ============================================
# COLUMNS DEMO
# ============================================

st.divider()
st.header("st.columns() - Column Layout Demo")
st.write("st.columns(number) - Creates side-by-side columns")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Column 1**")
    st.write("Content in first column")

with col2:
    st.write("**Column 2**")
    st.write("Content in second column")

with col3:
    st.write("**Column 3**")
    st.write("Content in third column")

# Different width columns
st.write("Different widths: st.columns([2,1,1])")
colA, colB, colC = st.columns([2, 1, 1])

with colA:
    st.write("**Width weight 2**")
    st.write("This column is wider")

with colB:
    st.write("**Width weight 1**")
    st.write("Narrower")

with colC:
    st.write("**Width weight 1**")
    st.write("Narrower")

# ============================================
# EXPANDER DEMO
# ============================================

st.divider()
st.header("st.expander() - Expandable Section")
st.write("st.expander('label') - Creates expandable section that hides/shows content")

with st.expander("📖 Click to expand this section"):
    st.write("This content is hidden until you click the expander!")
    st.write("You can put any widgets or content inside an expander.")
    st.success("Great for organizing long pages!")

with st.expander("📊 Another expander example"):
    st.dataframe(pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Score': [85, 92, 78]
    }))

with st.expander("💡 Tip"):
    st.markdown("Use expanders to hide detailed information and keep your page clean!")

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
    st.write(f"You selected: **{selected}**")
    
    if selected == "Home":
        st.write("🏠 Welcome to Home section")
    elif selected == "Data":
        st.dataframe(pd.DataFrame({'X': [1,2,3], 'Y': [4,5,6]}))
    elif selected == "Charts":
        st.line_chart(data=pd.DataFrame({'values': [10,20,15,30,25]}))
        
except ImportError:
    st.write("⚠️ streamlit-option-menu not installed.")
    st.write("Run: **pip install streamlit-option-menu**")
    st.code("""
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title="Main Menu",
    options=["Home", "Data", "Charts"],
    icons=["house", "table", "bar-chart"],
    default_index=0,
)
    """)
