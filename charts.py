# drawing line chart
import streamlit as st 
import pandas as pd
import numpy as np

st.title("Charts and Map")
st.subheader("Line Chart")
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.line_chart(chart_data)

st.subheader("Map")
# drawing a map
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
