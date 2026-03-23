import streamlit as st
from bs4 import BeautifulSoup
import requests

# Youtube Keyword Extractor
st.markdown("<h1 style='text-align:center;'>Youtube Keywords Extractor",unsafe_allow_html=True)
st.markdown("---",unsafe_allow_html=True)
url = st.text_input("Enter YouTube URL")

if url:   
        page = requests.get(url)
        page.encoding = 'utf-8'
        soup = BeautifulSoup(page.content, 'lxml')
        meta_tag = soup.select("meta[name='keywords']")
        keywords=meta_tag[0]["content"]
        st.title("Tags")
        st.markdown(f"<h4 style='color: #101820FF'>{keywords}</h4>",unsafe_allow_html=True)
        