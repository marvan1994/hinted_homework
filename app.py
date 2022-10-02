import pandas as pd
import numpy as np

import streamlit as st
import streamlit.components.v1 as components

import os

import json

from load_css import local_css

if 'task_number' not in st.session_state:
    st.session_state['task_number'] = 1
    st.session_state.progress = 0
    st.session_state.main_page = True
    st.session_state.task_page = False



st.set_page_config(page_title='Домашка с подсказками')

local_css("style.css")


#my_bar = st.progress(0)

def next_task_button():
    ### callback function for next_task button ###
    st.session_state.task_number += 1

with open('task_json.json') as f:
    task_dict = json.load(f)


placeholder_1 = st.empty()
placeholder_2 = st.empty()
placeholder_3 = st.empty()
placeholder_4 = st.empty()
placeholder_5 = st.empty()

def main_page():
    if st.session_state.main_page:
        placeholder_1.markdown('### Привет, Мастер! ### \n Это тестовый вариант домашнего задания, в котором тебе будет предложено решить 10 номеров с особыми подсказками')
        go_button = placeholder_2.button('Поехали?👌')
        if go_button:
            st.session_state.main_page = False
            st.session_state.task_page = True
            task_page()
    else:
        if st.session_state.task_page:
            task_page()
        else:
            last_page()

def task_page(task_dict = task_dict):

    number = st.session_state.task_number
    m_number = int(list(task_dict['task'].keys())[-1])

    if number >0:
        try:
            task = task_dict['task'][str(number)]
            solution = task_dict['solution'][str(number)]
            umit = task_dict['umit'][str(number)]
            umit_id = task_dict['umitsistem_id'][str(number)]


            placeholder_1.button('Следующая задача', key='next_task', on_click=next_task_button())
            placeholder_2.progress(number / m_number)
            placeholder_3.markdown(f'Задача {number}')
            placeholder_4.markdown(f'{task}', unsafe_allow_html=True)

            umits = [f'[{x}](https://www.google.com/)' for x in umit.split(',')]
            st.write(',   '.join(umits)                )


        except:
            st.balloons()
            st.session_state.task_page = False
            last_page()
def last_page():
    placeholder_1.markdown('Ты великолепен!')
main_page()




