import streamlit as st
import pandas as pd
import numpy as np

st.title('Data elements 둘러보기')
st.header('1. Dataframe', divider='rainbow') # divider=True

df = pd.DataFrame({'Col1':[1,2,3,4],
                   'Col2':[10,20,30,40]})

st.write(df)
with st.echo():
    st.dataframe(df, use_container_width=True) # 폭에 맞게 넓게 분배

df1 = pd.DataFrame(
    np.random.randn(5,10),
    columns = ['col_%d' % (i+1) for i in range(10)]
)
st.dataframe(df1)
st.dataframe(df1, width=400, height=200)
st.dataframe(df1, width=400, height=150, hide_index=True)
st.dataframe(df1, width=400, height=150, use_container_width=True) # width 400정했지만 무시

st.dataframe(df, column_order=('Col2','Col1'))

st.dataframe(df1.style.highlight_max(axis=0))
st.dataframe(df1.style.highlight_max(axis=1))
st.dataframe(df1.style.highlight_min(axis=0))
st.dataframe(df1.style.highlight_min(axis=1))

st.divider()

df2 = pd.DataFrame(
    [{'command' : 'st.write', 'rating' : 4, 'is_widget' : False},
     {'command' : 'st.dataframe', 'rating' : 5, 'is_widget' : True},
     {'command' : 'st.time_input', 'rating' : 3, 'is_widget' : True},
     {'command' : 'st.metric', 'rating' : 4, 'is_widget' : True}]
)
st.write(df2)
st.dataframe(df2, use_container_width=True)

st.markdown('엑셀파일을 읽어 데이터프레임 생성')
df3 = pd.read_excel('data/kor_news_240326.xlsx')
df3_part = df3.iloc[:100]
st.dataframe(df3_part, hide_index=True)

st.subheader('add_rows()')
df3_part1 = df3.iloc[:10]
df3_part2 = df3.iloc[20:30]

out_df = st.dataframe(df3_part1)
out_df.add_rows(df3_part2)

st.header('2. data editor : st.data_editor()')
edited_df = st.data_editor(df2)
fav_com = edited_df.loc[edited_df['rating'].idxmax()]['command']
st.markdown(f'가장 높은 점수의 위젯은? :red[{fav_com}] :+1:')

edited_df3 = st.data_editor(df3_part)

st.markdown('num_rows=dynamic') # default = 'fixed'
st.data_editor(df3_part1, num_rows = 'dynamic')

st.markdown('disabled = [col,...]')
st.data_editor(df2, disabled=['command', 'is_widget'])

st.header('3. table : st.table()')
st.table(df3_part.iloc[:3])

out_table = st.table(df3_part1.iloc[:2])
out_table.add_rows(df3_part2.iloc[:2])
