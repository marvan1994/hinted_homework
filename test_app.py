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


