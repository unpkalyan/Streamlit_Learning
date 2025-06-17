#import streamlit as st

#st.title('🎈 App Name')

#st.write('Hello world!')


import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World!")

with st.sidebar:
    st.header("About this app")
    st.write("This is my first Streamlit app and its LIT")

st.header("This is a header with a divider", divider="rainbow")

st.markdown("This is some more text added using the markdown function of streamlit")

st.subheader("streamlit columns")
col1, col2 = st.columns(2)

with col1:
    x = st.slider("Choose a value for x", 1, 10)

with col2:
    st.write("You have selected : ", x)


st.subheader("streamlit area chart using random data")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

st.subheader("streamlit bar chart using random data")
st.bar_chart(chart_data)
