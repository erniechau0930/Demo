import streamlit as st


st.title("Contact Info Collector App")
st.write("This app helps you collect Contact Info") 
st.write("Please fill in the following form:")

with st.form(key = "my_form"):
  first_name = st.text_input("Enter your first name:")
  last_name = st.text_input("Enter your last name:")
  favorite_number = st.number_input("Enter your favorite number:", step=1)
  
  if st.form_submit_button("Register"):
    if first_name.strip() == "" or last_name.strip() == "":
            st.error("Please enter both your first and last name!")
    else:
            st.success(f"Registration Success,Thank you!")
            with open("contacts.csv", "a") as f:
                f.write(f"{first_name},{last_name},{favorite_number}\n")
            st.success(f"Registration Success!")
          
st.header("### Registered Contacts")

try:
    with open("contacts.csv", "r") as f:
        lines = f.readlines()
        
        if lines:
            data_table = []
            for line in lines:
                data_table.append(line.strip().split(","))
            st.table(data_table)
        else:
            st.info("The file is empty.")

except FileNotFoundError:
    st.info("No contacts registered yet.")
