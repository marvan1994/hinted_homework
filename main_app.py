import streamlit as st

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

st.set_page_config(initial_sidebar_state='collapsed')
st.markdown('''<style> 
 .css-6qob1r {
        display: none;
    } </style> ''', unsafe_allow_html=True)
st.markdown('### Привет, Мастер! ### \n Это тестовый вариант домашнего задания, в котором тебе будет предложено решить 10 номеров с особыми подсказками')
bu = st.button('Поехали?👌')
if bu == True:
    switch_page("page1")