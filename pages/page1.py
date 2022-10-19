import streamlit as st
import json
import streamlit.components.v1 as components
#from streamlit_player import st_player
# from bokeh.models.widgets import Div

####################### CONFIGS ##########################
st.set_page_config(initial_sidebar_state='collapsed', layout="wide")
st.markdown('''<style> 
 .css-6qob1r {
        display: none;
    }
     
.css-y4qlto {
             display: none;}
</style> ''', unsafe_allow_html=True)


def run_hint(state):
    if state == 'Статья':

        umit = task_dict['umit'][str(number)]
        umit_id = task_dict['umitsistem_id'][str(number)]

        for x in umit.split('##'):
            umit_name = x.replace('\n', '_')
            st.write(f"[{umit_name}]({link})")

        with open('post_element.txt', encoding='utf-8') as file:
            element = ''.join(file.readlines())
        element = element.replace('/library/wp-content/', 'https://umschool.net/library/wp-content/')
        template = f'<div style = "overflow-y: scroll;" >{element}< / div >'
        # components.html(template)
        components.html(template, height=1000, scrolling=True)
    else:
        st.markdown('<iframe width="80%" height=400px src="https://www.youtube.com/embed/tgbNymZ7vqY"></iframe>',
                    unsafe_allow_html=True)


def umit_button(button):
    pass


def switch_page(page_name: str):
    from streamlit import _RerunData, _RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("main_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")


if 'task_number' not in st.session_state:
    st.session_state['task_number'] = 1

def next_task():
    st.session_state.task_number +=1

with open('data_task_json.json', encoding='utf-8') as f:
    task_dict = json.load(f)


col1, col2= st.columns([3,2])


link = '''https://umschool.net/library/himiya/periodicheskij-zakon-i-periodicheskaya-sistema-himicheskih-elementov-d-i-mendeleeva/#%D0%BF%D0%BE%D0%BD%D1%8F%D1%82%D0%B8%D0%B5_%D0%BE%D0%BA%D0%B8%D1%81%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE_%D0%B2%D0%BE%D1%81%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D1%85_%D1%81%D0%B2%D0%BE%D0%B9%D1%81%D1%82%D0%B2'''

number = st.session_state.task_number

m_number = int(list(task_dict['task'].keys())[-1])

if number < m_number:

    with col1:

        try:
            with st.form('task_form'):
                placeholder_1 = st.empty()
                placeholder_2 = st.empty()
                placeholder_3 = st.empty()
                placeholder_4 = st.empty()

                task = task_dict['task'][str(number)]
                solution = task_dict['solution'][str(number)]
                placeholder_2.progress(number / m_number)
                placeholder_3.markdown(f'Задача {number}')
                placeholder_4.markdown(f'{task}', unsafe_allow_html=True)
                ans = st.text_input('Введите ответ:','...')
                submit = st.form_submit_button('Записать ответ')
                if submit and len(ans) != '...':
                    print(ans)
                    next_task()
                    print(number)

        except:
            pass

    with col2:
        with st.form('radio'):
            state = st.radio('Формат подсказки', ['Статья','Вебинар'])
            hint_submission = st.form_submit_button('Показать подсказку')
        if hint_submission:
            run_hint(state)


