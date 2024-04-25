import numpy as np
import pandas as pd
import time
import streamlit as st

st.header('Data Column Config')
st.subheader('1. Column')
df = pd.DataFrame(
    [{'command' : 'st.write', 'rating' : 4, 'is_widget' : False},
     {'command' : 'st.dataframe', 'rating' : 5, 'is_widget' : True},
     {'command' : 'st.time_input', 'rating' : 3, 'is_widget' : True},
     {'command' : 'st.metric', 'rating' : 4, 'is_widget' : True}]
)

st.dataframe(df)
st.markdown('column(label=, help=, width=)')
st.dataframe(df,
             column_config = {
                 'command' : st.column_config.Column(
                     label = 'Streamlit Commands',
                     help = 'Streamlit **widget** commands',
                     width = 'medium'
                 )
             } )
st.markdown('column(label=, help=, width=, disabled=)')
st.data_editor(df,
               column_config = {
                'command' : st.column_config.Column(
                    label = 'Streamlit Commands',
                    help = 'Streamlit **widget** commands',
                    width = 'medium',
                    disabled=True
                 )
               }
               )
st.subheader('2. Text Column')
st.markdown('TextColumn(default=)')
st.data_editor(df,
               column_config = {
                'command' : st.column_config.TextColumn(
                    label = 'Streamlit Commands',
                    help = 'Streamlit **widget** commands',
                    default = 'st.'
                 )
               },
               num_rows='dynamic'
               )
# 새로운 행 추가했을 때 default 값 보여짐

st.markdown('TextColumn(max_chars=)')
st.data_editor(df,
               column_config = {
                'command' : st.column_config.TextColumn(
                    label = 'Streamlit Commands',
                    help = 'Streamlit **widget** commands',
                    default = 'st.',
                    max_chars=20
                 )
               },
               num_rows='dynamic'
               )

st.markdown('TextColumn(validate=)')
st.data_editor(df,
               column_config = {
                'command' : st.column_config.TextColumn(
                    label = 'Streamlit Commands',
                    help = 'Streamlit **widget** commands',
                    default = 'st.',
                    max_chars=20,
                    validate='^st\.[a-z_]+$'
                 )
               },
               num_rows='dynamic'
               )

st.subheader('3. Number Column')
st.data_editor(df,
               column_config = {
                   'rating' : st.column_config.NumberColumn(
                       label= '좋아요',
                       help = '한달동안의 좋아요수',
                       min_value = 0,
                       max_value = 10,
                       step = 0.5,
                       format = '%f'
                   )
               })

st.subheader('4. Checkbox Column')
st.data_editor(df,
               column_config = {
                   'is_widget' : st.column_config.CheckboxColumn(
                       label = '위젯인가?',
                       default = False
                   ),
                    'command' : st.column_config.TextColumn(
                        label = 'Streamlit Commands',
                        help = 'Streamlit **widget** commands',
                        default = 'st.',
                        max_chars=20,
                        validate='^st\.[a-z_]+$'
                 )
               },
               num_rows='dynamic')


data_df = pd.DataFrame(
    {
        "category": [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "📊 Data Exploration",
        ],
    }
)

st.subheader('5. Selectbox Column')
df2 = pd.DataFrame(
    {
        "category": [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "📊 Data Exploration",
        ],
    }
)

st.data_editor(df2)

st.data_editor(
    df2,
    column_config={
        "category": st.column_config.SelectboxColumn(
            "App Category",
            help="The category of the app",
            width="medium",
            options=[
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
            ],
            required=True,
        )
    },
    hide_index=True,
)

from datetime import datetime, date, time

st.subheader('6. Datetime Column')
df3 = pd.DataFrame(
    {'meeting_date' :
     [datetime(2024, 2, 5, 12, 30),
      datetime(2024, 2, 21, 2, 30),
      datetime(2024, 3, 22, 10, 00),
      datetime(2024, 3, 4, 11, 00),
      datetime(2024, 4, 9, 10, 30)]}
)

st.data_editor(df3)

st.data_editor(df3,
               column_config={
                    'meeting_date' : st.column_config.DatetimeColumn(
                        min_value = datetime(2024,1,1),
                        max_value = datetime(2024, 4, 10),
                        format = 'D MMM YYYY, h:mm a'
                    )
                   })
# MMM -> 영문 표기

st.subheader('7. Date Column')
df4 = pd.DataFrame(
    {'meeting_date' :
     [date(2024, 2, 5),
      date(2024, 2, 21),
      date(2024, 3, 22),
      date(2024, 3, 4),
      date(2024, 4, 9)]}
)
st.dataframe(df4)
st.data_editor(df4,
               column_config = {
                'meeting_date': st.column_config.DateColumn(
                    min_value=date(2023,1,1),
                    max_value=date(2025,12,31),
                    format='YYYY/MM/DD'
                )
                })

st.subheader('8. Time Column')
df5 = pd.DataFrame(
    {'meeting_date' :
     [time(12,30),
      time(2, 30),
      time(10, 00),
      time(11, 00),
      time(10, 30)]}
)
st.data_editor(df5,
               column_config = {
                   'meeting_date': st.column_config.TimeColumn(
                       min_value = time(9,0,0),
                       max_value = time(18,0,0),
                       format = 'hh:mm a'
                   )
               })

st.subheader('9. List Column')
df6 = pd.DataFrame(
    {
        'score' : [[0,4,60,80,100],
                   [80,30,80,50,70],
                   [90,30,60,80,100]
        ]
    }
)
st.dataframe(df6)

st.data_editor(df6,
             column_config={
                 'score' : st.column_config.ListColumn(
                    width = 'medium'
                 )
             })
# 이 경우는 data_editor, dataframe 모두 수정불가

st.table(df6)

st.subheader('10. Link Column')
df7 = pd.DataFrame(
    {
        'site' : ['naver','daum','google'],
        'url' : ['https://www.naver.com',
                 'https://www.daum.net',
                 'https://www.google.com']
    }
)
st.dataframe(df7)
st.data_editor(df7,
               column_config ={
                   'url' : st.column_config.LinkColumn(
                       help = 'Search portal site',
                       max_chars = 100,
                       validate = '^https://www\.[a-z]+\.[a-z]+',
                       display_text = 'Search site'
                   )
               })

st.subheader('11. LineChart Column / AreaChart Column / BarChart Column')
df8 = pd.DataFrame(
    {
        'name' : ['Kim','Lee','Choi'],
        'score' : [[0,4,60,80,100],
                   [80,30,80,50,70],
                   [90,30,60,80,100]
        ],
        'score2': [[0,4,60,80,100],
                   [80,30,80,50,70],
                   [90,30,60,80,100]],
        'score3': [[0,4,60,80,100],
                   [80,30,80,50,70],
                   [90,30,60,80,100]]
    }
)
st.dataframe(df8,
             column_config = {
                 'score2' : st.column_config.LineChartColumn(
                     y_min = 0,
                     y_max = 100
                 ),
                 'score3' : st.column_config.AreaChartColumn(
                     y_min = 0,
                     y_max = 100
                 ),
                 'score' : st.column_config.BarChartColumn(
                     y_min = 0,
                     y_max = 100
                 )
             })

st.subheader('12. Image Column')
df9 = pd.DataFrame(
    {
        "image": [
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png",
        ],
        # 'image_path':[
        #     'img/apple.png',
        #     'img/banana.jpg',
        #     'img/mango.jpg',
        #     'img/FuBao.jpg'
        # ]
    }
)
st.data_editor(df9,
             column_config = {
                 'image' : st.column_config.ImageColumn(
                     width = 'large'
                 )
                 # 'image_path': st.column_config.ImageColumn()
             })
# LinkColumn 하면 링크 클릭 시 이미지 보임
# img 폴더에 파일 넣어놓고 주소 지정하고 ImageColumn 형태로 써주면 된다
# 아니면 이미지 상대 주소주거나

st.subheader('13. Progress Column')
df10 = pd.DataFrame(
    {
        'sales' : [100, 50, 60, 80]
    }
)
st.data_editor(df10,
               column_config={
                   'sales':st.column_config.ProgressColumn(
                       min_value = 0, max_value = 150,
                       format = '%f만원'
                   )
               })

st.image('static/apple.png')
