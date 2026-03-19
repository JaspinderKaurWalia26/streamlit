import streamlit as st 
import time
# layout
# sidebar
# Add a selectbox to the sidebar
add_selectbox=st.sidebar.selectbox('How would you like to be contacted?',('Email','Home Phone','Mobile Phone'))

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# st.columns
left_column, right_column = st.columns(2)
left_column.button('Press me!')
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

# to show progress- st.progress
latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)


