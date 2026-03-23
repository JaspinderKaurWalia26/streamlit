import streamlit as st 
import pandas as pd
import time
from transformers import pipeline

#Title
st.title("Working with Caching and Session State")
@st.cache_data
def read_data():
    df=pd.read_csv("https://github.com/laxmimerit/All-CSV-ML-Data-Files-Download/raw/refs/heads/master/IMDB-Dataset.csv")
    return df.head()

start=time.time()
df=read_data()
st.write(time.time()-start)
st.button("Refresh It")

def update_session_state():
    if 'counter' not in st.session_state:
        st.session_state.counter=0
    st.write("Counter: ",st.session_state.counter)
    st.session_state.counter+=1
    
update_session_state()
    
@st.cache_resource
def load_model():
    model=pipeline("sentiment-analysis",model="distilbert-base-uncased-finetuned-sst-2-english")
    st.success("Loaded the NLP Model")
    return model

start_model=time.time()
model=load_model()
st.write(time.time()-start_model)
st.success("Got the model")