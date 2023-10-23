import streamlit as st
import pandas as pd
import numpy as np


data = pd.read_csv('b631bf23-204c-4ed9-b55d-0499a8087859_Data.csv', encoding='cp1251')
data2 = pd.read_csv('b631bf23-204c-4ed9-b55d-0499a8087859_Series - Metadata.csv', encoding='cp1251')
data3 = pd.read_csv('rankings.csv', encoding='cp1251')
data4 = pd.read_csv('DTF.csv', encoding='cp1251')
st.dataframe(data=data)
st.dataframe(data=data2)
st.dataframe(data=data3)
st.dataframe(data=data4)
# https://archive.doingbusiness.org/en/methodology
