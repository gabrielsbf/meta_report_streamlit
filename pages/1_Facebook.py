import streamlit as st
import datetime
import altair as alt
from make_dfs import *

st.set_page_config("Hub - Analytics Movementes", layout='wide')
st.header("Relatório Facebook")
since, until = st.columns(2)
since = since.date_input("Selecione a data do início da pesquisa", on_change=None)
until = until.date_input("Selecione a data do final da pesquisa", on_change=None)
since_formated = since.strftime("%d/%m/%Y")
until_formated = until.strftime("%d/%m/%Y")
st.subheader(f":bookmark_tabs: Relatório dos períodos de {since_formated}, até {until_formated}", divider='orange')
#Colocar um botão e usar sentença if para ele
if st.button("Gerar"):
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
    reactions = posts_df[['like','haha','love', 'sorry', 'wow', 'anger', 'created_time']].copy()
    reactions['created_time'] = reactions['created_time'].dt.strftime('%d/%m/%Y')
    st.bar_chart(reactions, x='created_time', use_container_width=True)


    table = posts_df.drop(columns=['haha','like','love', 'wow', 'anger', 'sorry'])

#Tabela
    st.data_editor(table,
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
                    "engaged_users": st.column_config.NumberColumn(
                        "us. engaj.", format="%d"
                    ),
                    "engaged_fans": st.column_config.NumberColumn(
                        "seg. engaj.", format="%d"
                    )
                })
