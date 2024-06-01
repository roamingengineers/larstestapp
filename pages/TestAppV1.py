import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

#st.write("home page test")


import streamlit as st

# Initialize session state variables
if 'total_flights' not in st.session_state:
    st.session_state['total_flights'] = 0
if 'total_time_minutes' not in st.session_state:
    st.session_state['total_time_minutes'] = 0
if 'total_time_seconds' not in st.session_state:
    st.session_state['total_time_seconds'] = 0
if 'page' not in st.session_state:
    st.session_state['page'] = 'main'

def main():
    st.title("Stair Climbing Tracker")
    
    if st.session_state['page'] == 'main':
        show_main()
    elif st.session_state['page'] == 'log_climb':
        show_log_climb()
    elif st.session_state['page'] == 'eiffel_tower':
        show_eiffel_tower()

def show_main():
    if st.button('Log Climb'):
        st.session_state['page'] = 'log_climb'
        st.experimental_rerun()  # Re-run the script to apply the page change
    if st.button('View Eiffel Tower Info'):
        st.session_state['page'] = 'eiffel_tower'
        st.experimental_rerun()  # Re-run the script to apply the page change

    st.subheader("Total Stats")
    st.write(f"Total Flights Climbed: {st.session_state['total_flights']}")
    st.write(f"Total Time: {st.session_state['total_time_minutes']:02d}:{st.session_state['total_time_seconds']:02d}")
    progress_percent = (st.session_state['total_flights'] / 1200) * 100
    st.write(f"Progress: {progress_percent:.2f}%")
    st.progress(progress_percent / 100)
    remaining_flights = 1200 - st.session_state['total_flights']
    st.write(f"Remaining Flights: {remaining_flights}")

def show_log_climb():
    with st.form(key='stair_form'):
        flights = st.number_input('Flights of Stairs:', min_value=1, step=1)
        time = st.text_input('Time:')
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            try:
                minutes, seconds = map(int, time.split(':'))
                st.session_state['total_flights'] += flights
                st.session_state['total_time_minutes'] += minutes
                st.session_state['total_time_seconds'] += seconds

                if st.session_state['total_time_seconds'] >= 60:
                    st.session_state['total_time_minutes'] += st.session_state['total_time_seconds'] // 60
                    st.session_state['total_time_seconds'] = st.session_state['total_time_seconds'] % 60

                st.success("Climb logged successfully!")
                st.session_state['page'] = 'main'
                st.experimental_rerun()  # Re-run the script to go back to the main page
            except ValueError:
                st.error("Please enter time in MM:SS format.")

    st.button('Back', on_click=lambda: change_page('main'))

def show_eiffel_tower():
    st.write("Eiffel Tower Info: The Eiffel Tower has approximately 1200 steps to the top.")
    st.button('Back to Main', on_click=lambda: change_page('main'))

def change_page(page):
    st.session_state['page'] = page
    st.experimental_rerun()  # Re-run the script to apply the page change

if __name__ == '__main__':
    main()
