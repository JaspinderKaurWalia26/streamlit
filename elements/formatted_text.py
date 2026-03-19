import streamlit as st  
# st.badge
st.badge("New")
st.badge("Success",icon=":material/check:",color="green")

# st.caption
st.caption("This is a string")

#st.code
code=''' def greet():
print("Good Moring") '''
st.code(code,language="python")

# st.divider
st.divider()

# st.echo

def get_user_name():
    return 'John'

with st.echo():
    def get_punctuation():
        return '!!!'
    
    
    greetings="Hi there,"
    value=get_user_name()
    punctuation=get_punctuation()
    
    st.write(greetings,value,punctuation)
    
#st.text

st.text("This is the text")

# utilities
# st.help
import pandas as pd
st.help(pd.DataFrame)

# st.html
st.html("<i> Hello")
    