import streamlit as st

st.title('Input Widgets!')
st.header('1. Button elements')
st.subheader('Button')
st.button('초기화', type='primary')
if st.button('안녕'):
    st.write('반가워 :smile:')
else:
    st.write('잘가! :raising_hand:')
# 버튼 누르지 않으면 False, 누르면 True

st.subheader('Link Button')
st.link_button('google', 'https://www.google.com')

st.subheader('Page Link Button', divider=True)
st.page_link('app.py',label = 'Home', icon = '🏠')
st.page_link('pages/1_Text_elements.py',
             label = 'Text elements')
st.page_link('pages/2_Data_elements.py',
              label = 'Data elements')
st.page_link('pages/박인화_streamlit연습문제.py',
              label = 'Exercise',
              disabled=True)
st.page_link('https://docs.streamlit.io/develop/api-reference',
              label = 'Streamlit Docs', icon ='🌎')

st.divider()
st.subheader('Form Submit_Button')
with st.form(key='form1'):
    id = st.text_input('ID')
    pw = st.text_input('Password', type='password')
    submitted = st.form_submit_button('로그인')
    if submitted:
        st.write('id :', id, 'pw : ', pw)
# if 부분을 바깥영역에 써주면, 로그인 버튼 눌렀을 때 출력 내용이 바깥영역에 출력됨

form = st.form(key='form2')
title = form.text_input('제목')
contents = form.text_area('질의응답')
assign = form.form_submit_button('등록')
if assign:
    form.write(f'제목:{title}, 질문:{contents}')
#st.write로 하면 바깥영역에 내용 출력

st.header('2. Selection elements', divider=True)
st.subheader('Checkbox')
agree = st.checkbox('찬성', value=True, label_visibility='visible')
if agree:
    st.write('Good')

st.subheader('Toggle')
on = st.toggle('선택')
if on:
    st.write('on')

st.subheader('Radio')
fruit = st.radio(
    label = '좋아하는 과일은?',
    options = [':banana:바나나',':strawberry:딸기',':melon:메론',':apple:사과',':pear:배'],
    captions = ['웃어요','달콤해요','시원해요','상큼해요','즙이많아요'],
    horizontal=True, index=1
)
if fruit ==':banana:바나나':
    st.write('바나나를 선택했어요!')
else:
    st.write('바나나가 아니군요')

st.subheader('Selectbox')
fruit = st.selectbox(label='과일을 선택하세요',
             options = ['banana','strawberry','apple','melon'],
                     index=None, placeholder='Choose your favorite fruit!',
                     label_visibility = 'collapsed')
st.write(f'당신의 최애 과일은 {fruit}이군요~ :smile:')


st.divider()
# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

st.divider()

st.subheader('Multiselect')
colors = st.multiselect('당신이 좋아하는 색깔은?',
                         options = ['red','green','blue','yellow','pink'],
                         default = ['green','pink']
                        )
st.write('선택한 색상은 ', colors)

st.subheader('Selectslider')
colors = st.select_slider('당신이 좋아하는 색상은',
                 options = ['red','green','blue','yellow','pink',
                            'violet','indigo', 'orange'])
st.write('당신이 좋아하는 색상은', colors)

colors = st.select_slider('당신이 좋아하는 색상은',
                 options = ['red','green','blue','yellow','pink',
                            'violet','indigo', 'orange'],
                value = 'blue')
st.write('당신이 좋아하는 색상은', colors)

color_st, color_end = st.select_slider('당신이 좋아하는 색상은',
                 options = ['red','green','blue','yellow','pink',
                            'violet','indigo', 'orange'],
                value = ('blue', 'pink'))
# () 튜플 형태로 나오니 unpacking 가능
st.write('당신이 좋아하는 색상은', color_st, color_end)

st.subheader('Colorpicker')
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

st.header('3. Numeric Input elements')
st.subheader('Number input')
num = st.number_input('숫자입력')
st.write(num)

num = st.number_input('숫자입력', value=None, 
                      placeholder = '숫자를 입력하세요')
st.write(f'현재숫자: {num}')

num = st.number_input('숫자입력', min_value=-10.0,
                      max_value = 10.0, step=0.05,
                      format='%.2f'
                      )
st.write(f'현재숫자: {num:.2f}')

st.subheader('Slider')
age = st.slider('나이', min_value=0, max_value=100, value=23, step=2)
st.write(age)

score = st.slider('점수대',
                  min_value=0.0, max_value=100.0, value=(60.0,100.0))
st.write(score)

st.divider()
st.header('4. Text Input elements')
st.subheader('Text input')
id = st.text_input(label = '아이디',value='id')
pw = st.text_input(label = '비밀번호', type='password')
st.write(f'아이다: {id}, 비밀번호: {pw}')

st.subheader('Text area')
text = st.text_area('질문을 입력하세요')
st.write(text)
st.write(len(text))

st.divider()
st.header('5. Date & Time input elements')
st.subheader('Date Input')

from datetime import datetime, date, time, timedelta

date = st.date_input(label = '일자 선택', value = date(2024,3,1),
                     min_value = date(2023, 1, 1),
                     max_value = date(2024,12,30),
                     format = 'YYYY.MM.DD')
st.write(date)

st.subheader('Time Input')
time = st.time_input('시간 입력',
              value = time(8,00),
                     step = timedelta(minutes=20))
st.write(time)

