import streamlit as st

st.header('Popover Container')

with st.popover('Open popover'):
    st.write('Hello')
    name = st.text_input('What\'s your name?')
st.write(f'Your name is {name} :sunglasses:')

popover = st.popover('Click', use_container_width=True)
popover.write('Why?')
black = popover.checkbox('black',True)
orange = popover.checkbox('orange',True)

if black:
    st.write('This is black')
if orange:
    st.write(':orange[This is orange]')

with st.popover('popover사용시 주의점'):
    st.write('popover를 또 다른 popover 안에 배치불가')
