from srcs.classes.social_man import Social_Manager
import streamlit as st
import datetime
from main import *

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
    col1,col2,col3 = st.columns(3)
    # ,col4,col5,col6,col7,col8,col9,col10,col11,col12
    col1.metric(label="Comentários", value=str(posts_df["comments"].sum()))
    col2.metric(label="Compartilhamentos", value=str(posts_df["shares"].sum()))
    col3.metric(label="Alcance", value=str(posts_df["reach"].sum()))

#Tabela
    st.data_editor(posts_df,
                column_config={
                    "permalink_url": st.column_config.LinkColumn(
                        "link",
                            help="link of the posts",
                            display_text="access post",
                            width=120
                    ),
                    "shares": st.column_config.NumberColumn(
                        "compartilhamentos",width="120", format="%d"
                    ),
                    "comments": st.column_config.NumberColumn(
                        "comentários",width="90", format="%d"
                    ),
                    "reach": st.column_config.NumberColumn(
                        "alcance",width=80, format="%d"
                    ),
                    "like": st.column_config.NumberColumn(
                        "like",width="small", format="%d"
                    ),
                    "haha": st.column_config.NumberColumn(
                        "haha",width="small", format="%d"
                    ),
                    "love": st.column_config.NumberColumn(
                        "love",width="small", format="%d"
                    ),
                    "sorry": st.column_config.NumberColumn(
                        "sorry",width="small", format="%d"
                    ),
                    "wow": st.column_config.NumberColumn(
                        "wow",width="small", format="%d"
                    ),
                    "anger": st.column_config.NumberColumn(
                        "anger",width="small", format="%d"
                    ),
                        "unique_clicks_on_post": st.column_config.NumberColumn(
                        "cliques únicos", format="%d"
                    ),
                    "engaged_users": st.column_config.NumberColumn(
                        "usuários engajados", format="%d"
                    ),
                    "engaged_fans": st.column_config.NumberColumn(
                        "seguidores engajados", format="%d"
                    )
                })


