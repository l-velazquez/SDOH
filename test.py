import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.express.colors as pc
import ssl
import json
from urllib.request import urlopen
from time import sleep

st.set_page_config(page_title='SDOH Puerto Rico', page_icon='🗺')
#import data
df = pd.read_csv("sdoh_v2.csv")
lab_test_cols = ["albumin_urine", "bun", "creatinine_serum", "creatinine_urine"]
selected_col = st.selectbox("Select lab test to map", lab_test_cols)
df = df[["lat", "lon", selected_col]]
# Map Figure Layout

title_html = '''
             <h1 style="font-size:28px;color:#444444;text-align:center;">SDOH Puerto Rico</h1>
             <h2 style="font-size:18px;color:#444444;text-align:center;"> Kidney Disease Lab Data </h2>
             '''         
st.markdown(title_html, unsafe_allow_html=True)
st.map(df,color="#32a877")