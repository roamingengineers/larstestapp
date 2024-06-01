import streamlit as st
import json
import os


st.set_page_config(page_title="Stair Climbing Tracker", page_icon="🗼")
# Path to the JSON file in the repository
USER_DATA_FILE = "userdata.json" 

st.title("Stair Climbing Tracker 🗼")
# Initialize session state variables
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

# Load user data from JSON file
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save user data to JSON file
def save_user_data(data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

user_data = load_user_data()

def main():
    if st.session_state['page'] == 'login':
        show_login()
    elif st.session_state['page'] == 'main':
        show_main()
    elif st.session_state['page'] == 'log_climb':
        show_log_climb()
    elif st.session_state['page'] == 'eiffel_tower':
        show_eiffel_tower()
    elif st.session_state['page'] == 'create_account':
        show_create_account()

def show_login():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in user_data and user_data[username]['password'] == password:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['page'] = 'main'
            st.rerun()
        else:
            st.error("Invalid username or password")

    if st.button("Create a Login"):
        st.session_state['page'] = 'create_account'
        st.rerun()

def show_create_account():
    st.header("Create a New Account")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Create Account"):
        if new_username in user_data:
            st.error("Username already exists. Please choose a different username.")
        elif new_password != confirm_password:
            st.error("Passwords do not match. Please try again.")
        elif not new_username or not new_password:
            st.error("Username and Password cannot be empty.")
        else:
            user_data[new_username] = {
                "password": new_password,
                "total_flights": 0,
                "total_time_minutes": 0,
                "total_time_seconds": 0
            }
            save_user_data(user_data)
            st.success("Account created successfully! Please log in.")
            st.session_state['page'] = 'login'
            st.rerun()

    st.button("Back to Login", on_click=lambda: change_page('login'))

def show_main():
    st.header(f"Welcome, {st.session_state['username']}")

    if st.button('Log Climb'):
        st.session_state['page'] = 'log_climb'
        st.rerun()
    if st.button('View Eiffel Tower Info'):
        st.session_state['page'] = 'eiffel_tower'
        st.rerun()
    if st.button('Logout'):
        st.session_state['logged_in'] = False
        st.session_state['username'] = ""
        st.session_state['page'] = 'login'
        st.rerun()

    user = user_data[st.session_state['username']]
    st.subheader("Total Stats")
    st.write(f"Total Flights Climbed: {user['total_flights']}")
    st.write(f"Total Time: {user['total_time_minutes']:02d}:{user['total_time_seconds']:02d}")
    progress_percent = (user['total_flights'] / 1200) * 100
    st.write(f"Progress: {progress_percent:.2f}%")
    st.progress(progress_percent / 100)
    remaining_flights = 1200 - user['total_flights']
    st.write(f"Remaining Flights: {remaining_flights}")

def show_log_climb():
    user = user_data[st.session_state['username']]
    with st.form(key='stair_form'):
        flights = st.number_input('Flights of Stairs:', min_value=1, step=1)
        time = st.text_input('Time (MM:SS):')
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            try:
                minutes, seconds = map(int, time.split(':'))
                user['total_flights'] += flights
                user['total_time_minutes'] += minutes
                user['total_time_seconds'] += seconds

                if user['total_time_seconds'] >= 60:
                    user['total_time_minutes'] += user['total_time_seconds'] // 60
                    user['total_time_seconds'] = user['total_time_seconds'] % 60

                save_user_data(user_data)
                st.success("Climb logged successfully!")
                st.session_state['page'] = 'main'
                st.rerun()
            except ValueError:
                st.error("Please enter time in MM:SS format.")

    st.button('Back', on_click=lambda: change_page('main'))

def show_eiffel_tower():
    st.write("Eiffel Tower Info: The Eiffel Tower has approximately 1200 steps to the top.")
    st.button('Back to Main', on_click=lambda: change_page('main'))

def change_page(page):
    st.session_state['page'] = page
    st.rerun()

if __name__ == '__main__':
    main()
