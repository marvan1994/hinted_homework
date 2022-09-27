import pandas as pd
import numpy as np

import streamlit as st

import os

import json

from load_css import local_css

if 'task_number' not in st.session_state:
    st.session_state['task_number'] = 1
    st.session_state['task_progress'] = 0.1

st.set_page_config(page_title='Домашка с подсказками')

local_css("style.css")


#my_bar = st.progress(0)

if st.session_state.task_number < 10:
    button_text = 'Следующая задача'


next_task = st.button(button_text)

if next_task and button_text != 'Закончить':
    if st.session_state.task_number<10:
        st.session_state.task_progress +=0.1
        st.session_state.task_number +=1
    else:
        st.session_state.task_progress = 1.0
        button_text = 'Закончить'
elif next_task and button_text == 'Закончить':
    st.balloons()
else:
    pass


my_bar = st.progress(st.session_state.task_progress)

st.markdown(f'Задача {st.session_state.task_number}')
