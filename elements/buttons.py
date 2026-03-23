import streamlit as st 
# Creating buttons
st.markdown("<h3>Button</h3>",unsafe_allow_html=True)
state=st.button("Click Here")
if state:
    st.write("Button Pressed")

#st.download_button
#Downloading image
st.markdown("<h3>Download Image</h3>",unsafe_allow_html=True)
with open("image.jpeg", "rb") as file:
    st.download_button(
        label="Download image",
        data=file,
        file_name="image.jpeg",
        mime="image/jpeg",
    )
    
# Generating data on click
# Downloading data
import streamlit as st
import time
st.markdown("<h3>Click to download report</h3>",unsafe_allow_html=True)
def make_report():
    time.sleep(1)
    return "col1,col2\n1,2\n3,4".encode("utf-8")

st.download_button(
    label="Download report",
    data=make_report(),
    file_name="report.csv",
    mime="text/csv",
)

# Displaying a Link button
st.markdown("<h3>Linking the button</h3>",unsafe_allow_html=True)
st.link_button("Go to Streamlit Documentation","https://docs.streamlit.io/")