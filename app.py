import streamlit as st

st.set_page_config(
    page_title='Streamlit Practice',
    page_icon='😁',
    layout='wide',
    initial_sidebar_state = 'auto'
)

st.title('스트림릿 맛보기')

st.write('''
- Text elements  
- Data elements  
- Data Column configure    
- Chart elements  
- Input elements  
- Layout & Containers  
''')

# https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app
# https://docs.streamlit.io/develop/concepts/multipage-apps/pages-directory
# 멀티페이지 구성