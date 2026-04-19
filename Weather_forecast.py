import pickle as pkl
import streamlit as st
import numpy as np
import pandas as pd

## Give a Page Name and Icon of the App
st.set_page_config(page_title="Welcome Forecast App",page_icon="🌤️",layout='centered')

## Add Background color
st.markdown("""
    <style>
    .stApp {
        background-color: #E3F2FD; 
        color:#1A237E;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)



## Give a title of the app
st.title('🌤️Welcome to the Weather Prediction App')
st.subheader('Your personal AI weather assistant🤖')

st.write("""
This app predicts upcoming weather conditions using machine learning.  
Just enter temperature, humidity, wind speed, and other details —  
and get predict weather along with safety!""")

st.divider()

st.markdown('Ready to know your forecast?')
if st.button('Go to Weather Prediction'):
    st.switch_page('pages/Page_2_Weather_forecast.py')

st.markdown('----')



