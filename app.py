from srcs.classes.social_man import Social_Manager
import streamlit as st
from main import *

since = st.date_input("what is the begin date to filter", on_change=None)
until = st.date_input("what is the final date to filter", on_change=None)
st.write("a data é de", since, "até", until)
since_formated = since.strftime("%d/%m/%Y")
until_formated = until.strftime("%d/%m/%Y")
st.button("confirmar", on_click=print_df(since_formated,until_formated))
