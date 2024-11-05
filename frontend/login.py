import streamlit as st
import base64
from dl import user 
from dl_admin_page import admin_page  # 'dl.py' contains the logic for the 'upload_page'

# Function to convert a binary file to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Function to set background image using base64 encoding
def set_bg_image(image_file):
    bin_str = get_base64_of_bin_file(image_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bin_str}");
        background-size: contain;
        background-position: left;
        min-height: 100vh;
        background-repeat: no-repeat;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to create the login form
def login_form():
    set_bg_image('deep-fake.jpg')

    

    col1, col2, col3 = st.columns([2, 3, 4])
    with col3:
        st.title("Deep Fake Image Classification")
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        if st.button('Login'):
            # Admin user logic here
            if username == 'Admin' and password == 'admin_6732':
                st.session_state.authenticated = "upload_page"
                st.success("You are logged in as Admin")
                st.experimental_rerun()
            # Normal user login
            elif username == 'User' and password == 'user_9012':
                st.session_state.authenticated = "user_page"
                st.success("You are logged in as User")
                st.experimental_rerun()
            # When the authentication of username and password fails
            else:
                st.error("Incorrect password or username")

if __name__ == "__main__":
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = "login_page"

    if st.session_state.authenticated == "login_page":
        login_form()
    elif st.session_state.authenticated == "upload_page":
        admin_page()
    elif st.session_state.authenticated == "user_page":
        user()
