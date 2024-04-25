# 1. 뉴스 데이터를 dataframe으로 표시하기
# 2. 뉴스데이터의 url 컬럼을 실제 뉴스기사 페이지로 이동하도록 적절한 column configuration 사용
# 3. 분류 컬럼 중 대분류 컬럼에 대한 빈도를 bar chart로 그리기
# 4. 제목 컬럼에 대하여 텍스트 전처리를 진행한 결과를 토대로 경제, 사회 분야의 빈도가 많은 주요 키워드 20위를 bar chart로 그리기
import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
from konlpy.tag import Okt
import matplotlib.pyplot as plt
import seaborn as sns
# caching
file_path = 'data/kor_news_240326.xlsx'
def preprocess(df):
    df['분류리스트'] = df.분류.str.split('>')
    df['대분류'] = df['분류리스트'].str[0]
    df['중분류'] = df['분류리스트'].str[1]
    df['소분류'] = df['분류리스트'].str[2]
    return df

@st.cache_data
def load_data(file_path):
    df=pd.read_excel(file_path)
    return preprocess(df)
news = load_data(file_path)
st.dataframe(news)
###########################################
# st.subheader('1. 뉴스 데이터를 dataframe으로 표시하기')
# news = pd.read_excel('data/kor_news_240326.xlsx')
# st.dataframe(news)


st.divider()
st.subheader('2. 뉴스데이터의 url 컬럼을 실제 뉴스기사 페이지로 이동하도록 적절한 column configuration 사용')
st.data_editor(news,
               column_config={
                   'URL': st.column_config.LinkColumn(
                       help = 'article link',
                       max_chars = 200
                   )
               })


st.divider()
st.subheader('3. 분류 컬럼 중 대분류 컬럼에 대한 빈도를 bar chart로 그리기')

df = pd.DataFrame(news.대분류.value_counts())
st.bar_chart(df)


st.divider()
st.subheader('4. 제목 컬럼에 대하여 텍스트 전처리를 진행한 결과를 토대로 경제, 사회 분야의 빈도가 많은 주요 키워드 20위를 bar chart로 그리기')


def count_word(df, column_name):
    titles = list(df[column_name])
    okt = Okt()
    title_pos = [okt.pos(title) for title in titles]

    token_list = []
    for token_tag in title_pos:
        result = []
        for token, tag in token_tag:
            if (len(token) > 1) and (tag not in ['Punctuation', 'Josa', 'Number', 'Suffix', 'Foreign']):
                result.append(token)
        token_list.append(result)

    tokens = np.hstack(token_list)

    tokens_cnt = Counter(tokens)
    tokens_df = pd.DataFrame(pd.Series(tokens_cnt), columns=['Freq'])
    sorted_df = tokens_df.sort_values(by='Freq', ascending=False)
    return sorted_df


df_econo = news[news['대분류']=='경제']
df_econo_cnt = count_word(df_econo, '제목')
st.markdown('경제 분야 Top20 키워드')
st.bar_chart(df_econo_cnt.iloc[:20], color = '#f0f')

df_society = news[news['대분류']=='사회']
df_society_cnt = count_word(df_society, '제목')
st.markdown('사회 분야 Top20 키워드')
st.bar_chart(df_society_cnt.iloc[:20], color ="#0000ff")

