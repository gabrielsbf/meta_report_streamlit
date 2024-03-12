import streamlit as st
import datetime
import altair as alt
from make_dfs import *
from fpdf import FPDF
import base64

def header_section():
    st.set_page_config("Hub - Analytics Movementes", layout='wide')
    st.header("Relatório Facebook")

def date_input():
    since, until = st.columns(2)
    since = since.date_input("Selecione a data do início da pesquisa", on_change=None)
    until = until.date_input("Selecione a data do final da pesquisa", on_change=None)
    since_formated = since.strftime("%d/%m/%Y")
    until_formated = until.strftime("%d/%m/%Y")
    st.subheader(f":bookmark_tabs: Relatório dos períodos de {since_formated}, até {until_formated}", divider='orange')
    return [since_formated, until_formated]

header = header_section()
datas = date_input()
#Colocar um botão e usar sentença if para ele
if st.button("Gerar"):
    since_formated = datas[0]
    until_formated = datas[1]
    posts_df = df_face_report(since_formated, until_formated)
    col1,col2,col3,col4,col5,col6, = st.columns(6)

    col1.metric(label="Comentários", value=str(posts_df["comments"].sum()))
    col2.metric(label="Compartilhamentos", value=str(posts_df["shares"].sum()))
    col3.metric(label="Alcance", value=str(posts_df["reach"].sum()))
    col4.metric(label="Cliques Únicos", value=str(posts_df["unique_clicks_on_post"].sum()))
    col5.metric(label="Usuários Engajados", value=str(posts_df["engaged_users"].sum()))
    col6.metric(label="Seguidores Engajados", value=str(posts_df["engaged_fans"].sum()))


    col7,col8,col9,col10,col11,col12 = st.columns(6)
    col7.metric(label="react - haha", value=str(posts_df["haha"].sum()))
    col8.metric(label="react - wow", value=str(posts_df["wow"].sum()))
    col9.metric(label="react - like", value=str(posts_df["like"].sum()))
    col10.metric(label="react - love", value=str(posts_df["love"].sum()))
    col11.metric(label="react - sorry", value=str(posts_df["sorry"].sum()))
    col12.metric(label="react - anger", value=str(posts_df["anger"].sum() * -1))
    posts_df["time_parsed"] = posts_df["created_time"].dt.strftime("%d/%m/%Y")
    st.bar_chart(posts_df, x='time_parsed', y=['haha','wow', 'like', 'love', 'sorry', 'anger'])
    col13, col14 = st.columns(2)

    df_ag = posts_df.drop(columns=['created_time']).groupby(['time_parsed']).sum()
    df_ag.reset_index(names=['time_parsed'],inplace=True,col_level=0)
    # print(df_ag)
    # print(df_ag["love"])
    col13.line_chart(df_ag,x='time_parsed', y='reach')
    col14.line_chart(df_ag,x='time_parsed', y= 'engagment')

#Tabela
    table = posts_df.drop(columns=['haha','like','love', 'wow', 'anger', 'sorry', "engaged_fans", "engaged_users"])
    table_st = st.data_editor(table,
                column_config={
                    "created_time" : st.column_config.DatetimeColumn(
                        "data",
                        format="DD-MM-YYYY HH:mm:ss"
                    ),
                    "permalink_url": st.column_config.LinkColumn(
                        "link",
                            help="link of the posts",
                            display_text="access post",
                            width=120
                    ),
                    "shares": st.column_config.NumberColumn(
                        "compart.", format="%d"
                    ),
                    "comments": st.column_config.NumberColumn(
                        "coment.", format="%d"
                    ),
                    "reach": st.column_config.NumberColumn(
                        "alcance", format="%d"
                    ),
                    "positive_reactions": st.column_config.NumberColumn(
                        "reac. posit.", format="%d"
                    ),

                    "negative_reactions": st.column_config.NumberColumn(
                        "reac. negat.", format="%d"
                    ),
                    "unique_clicks_on_post": st.column_config.NumberColumn(
                    "cliques un.", format="%d"
                    ),
                    "engagment": st.column_config.NumberColumn(
                        "engajamento", format="%d",help='soma do total de compartilhamentos, comentários e reações, tanto positivas quanto negativas'
                    )
                },hide_index=True, column_order=["created_time","permalink_url","shares", "comments","reach",
                                                 "positive_reactions","negative_reactions","unique_clicks_on_post", "engagment"],
                use_container_width=True, height=len(posts_df) * 38)

