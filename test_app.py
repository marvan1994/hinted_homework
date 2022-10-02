import streamlit as st
from load_css import local_css

if 'task_number' not in st.session_state:
    st.session_state['task_number'] = 0
    st.session_state.first_page = True
    st.session_state.second_page = False

st.set_page_config(page_title='Тестовая страница')

local_css("style.css")

placeholder_1 = st.empty()
placeholder_2 = st.empty()


def first_page():
    if st.session_state.first_page:
        placeholder_1.write('first page')
        button_1 = placeholder_2.button('go to second page')
        if button_1:
            st.session_state.second_page = True
            second_page()
def second_page():
    if st.session_state.second_page:
        placeholder_1.write('second page')
        placeholder_2.empty()

first_page()

