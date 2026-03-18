import streamlit as st
import pandas as pd

# Text elements
st.title("My First App")
st.header("_Streamlit_ is cool :sunglasses:")
st.subheader("Learning is a process")
st.text("First step in learning the streamlit")
st.markdown("---")
st.markdown("**Hello** *World*")


# Display elements
st.write("## H2")
table=pd.DataFrame({"Column 1":[1,2,3,4,5,6,7],"Column 2":[11,12,13,14,15,16,17]})
st.table(table)
st.dataframe(table)

# Media Widgets
st.image("image.jpeg",caption="This is my image")

# Interactive Widgets
def change():
    print(st.session_state.checker)
# Checkbox
st.checkbox("Checkbox",value=True,on_change=change,key="checker")

# radio button
radio_btn=st.radio("In which Country do you live?",options=("US","UK","Canada"))

# button
def button_click():
    print("Button Clicked")
    
btn=st.button("Click Me!",on_click=button_click)

# selectbox
select=st.selectbox("What is your favourite car?",options=("BMW","Audi","Ferreri"))
multi_select=st.multiselect("What is your favourite car?",options=("BMW","Audi","Ferreri"))

# file uploader widget

# Single file upload
image=st.file_uploader("Please upload an image",type=["jpg","png"])
if image is not None:
    st.image(image)
    
# Multiple File upload
img=st.file_uploader("Please upload an image",type=["jpg","png"],accept_multiple_files=True)
if img is not None:
    st.image(img)
    
# slider
val=st.slider("This is a slider")
# setting min and max value in the slider
value=st.slider("This is another slider",min_value=50,max_value=150,value=80)

# Taking input from the user

# text_input field
small_input=st.text_input("Enter the Course Details")
print(small_input)

# text_area field
large_input=st.text_area("Enter the Course Description")
print(large_input)

# data_input field
date=st.date_input("Enter the registration date")
print(date)

# time_input field
time=st.time_input("Set Timer")
print(time)
 

