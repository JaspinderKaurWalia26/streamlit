import streamlit as st
import datetime
st.markdown("<h2>Exploring Streamlit</h2>",unsafe_allow_html=True)
#checkbox
st.markdown("<h4>Displaying Checkbox</h4>",unsafe_allow_html=True)
agree=st.checkbox("I agree")
if agree:
    st.write("Great")
    
#color selection
st.markdown("<h4>Choose a color</h4>",unsafe_allow_html=True)
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

# rating widget
st.markdown("<h4>Please do a rating</h4>",unsafe_allow_html=True)
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} stars.")
    
# multi select element
st.markdown("<h4>Select the options</h4>",unsafe_allow_html=True)
options = st.multiselect(
    "What are your favorite colors?",
    ["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"],
)

st.write("You selected:", options)

# Select multiple options from the provided options
st.markdown("<h4>Select multiple options from the provided options</h4>",unsafe_allow_html=True)
options = ["North", "East", "South", "West"]
selection = st.pills("Directions", options, selection_mode="multi")
st.markdown(f"Your selected options: {selection}.")

# st.radio
st.markdown("<h4>Select Option</h4>",unsafe_allow_html=True)
genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ]
    
)
if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")
    
# toggle
st.markdown("<h4>Displaying Toggle</h4>",unsafe_allow_html=True)
on = st.toggle("Activate feature")
if on:
    st.write("Feature activated!")
    
# Taking date as an input
date = st.date_input(
    "When's your birthday",
    value=None,
    min_value=datetime.date(1950, 1, 1),   # start year
    max_value=datetime.date.today()        # end year
)

st.write("Your birthday is:", date)

# Taking time as an input
time = st.time_input("Set an alarm for", value=None)
st.write("Alarm is set for", time)

# Taking prompt from the user
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

