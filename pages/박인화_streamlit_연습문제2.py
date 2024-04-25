import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import json
from konlpy.tag import Okt
import matplotlib.pyplot as plt
from collections import Counter
import folium
from streamlit_folium import st_folium

# @st.cache_datadef
# def load_iris():
#     iris = sns.load_dataset('iris')
#     return iris
# iris = load_iris()
# st.dataframe(iris)


iris = sns.load_dataset('iris')
with st.container():
    st.header('1. iris 데이터')
    st.subheader('1-1) iris 데이터셋을 데이터프레임으로 표시')
    st.dataframe(iris)

    st.divider()
    st.subheader('1-2) 품종(species)을 선택하면, 해당 품종의 데이터에 대한 데이터프레임으로 표시')
    species = st.multiselect('Select species~',
                            options=set(iris.species),
                             default = ['setosa']
                            )

    if species:
        df = iris[iris['species'].isin(species)]
        st.write(df)

    st.divider()
    st.subheader('1-3) 품종 제외한 4가지 컬럼을 선택하면 컬럼에 대한 히스토그램 그리기(matplotlib)')

    column = st.radio(
        label='어떤 컬럼의 데이터가 궁금한가요?',
        options= iris.columns[:-1],
        captions=['꽃받침 길이','꽃받침 너비','꽃잎 길이', '꽃잎 너비'],
        horizontal=True, index=1
    )
    if column:
        fig, ax = plt.subplots()
        ax.hist(iris[column])
        ax.set_title('Histogram')
        ax.set_xlabel(column)
        st.pyplot(fig)

with st.container():
    st.header('2. kor_news 데이터셋을 이용')
    st.subheader('2-1) 분류의 대분류 기준을 선택하면 해당 분야의 주요 키워드 20위에 대한 bar chart 표시')

    news = pd.read_excel('data/kor_news_240326.xlsx')
    news['분류리스트'] = news.분류.str.split('>')
    news['대분류'] = news['분류리스트'].str[0]
    news['중분류'] = news['분류리스트'].str[1]
    news['소분류'] = news['분류리스트'].str[2]
    def word_count(df,cat):
        titles = list(df[df['대분류']==cat]['제목'])
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

    categories = set(news['대분류'])
    cat = st.selectbox('대분류 선택하세요', options=categories)
    if cat:
        df = word_count(news,cat)[:20]
        st.bar_chart(df)

st.divider()
st.header('경기도인구데이터')
st.subheader('3-1) 연도별 인구수에 대한 지도 시각화, 2007년, 2015년, 2017년 연도를 탭(tab)으로 제시')

with open('data/경기도행정구역경계.json', encoding='utf-8') as f:
    geogg = json.loads(f.read())

df_gg = pd.read_excel('data/경기도인구데이터.xlsx', index_col='구분')

tab1, tab2, tab3 = st.tabs(['2007','2015','2017'])
with tab1:
    st.subheader('2007')
    map = folium.Map(location=[37.5666, 126.9782], zoom_start=8)
    folium.GeoJson(geogg).add_to(map)
    folium.Choropleth(geo_data=geogg,
                      data=df_gg[2007],
                      columns=[df_gg.index, df_gg[2007]],
                      key_on='feature.properties.name').add_to(map)
    st_folium(map, width=600, height=400, key=2005)
with tab2:
    st.subheader('2015')
    map = folium.Map(location=[37.5666, 126.9782], zoom_start=8)
    folium.GeoJson(geogg).add_to(map)
    folium.Choropleth(geo_data=geogg,
                      data=df_gg[2015],
                      columns=[df_gg.index, df_gg[2015]],
                      key_on='feature.properties.name').add_to(map)
    st_folium(map, width=600, height=400, key=2015)
with tab3:
    st.subheader('2017')
    map = folium.Map(location=[37.5666, 126.9782], zoom_start=8)
    folium.GeoJson(geogg).add_to(map)
    folium.Choropleth(geo_data=geogg,
                      data=df_gg[2017],
                      columns=[df_gg.index, df_gg[2017]],
                      key_on='feature.properties.name').add_to(map)
    st_folium(map, width=600, height=400, key=2017)


##########
# 모듈 불러오기
# from utils.map import load_data, load_geo_json, load_excel_data, draw_map

