import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.write(
   "https://www.data.go.kr/data/15069309/fileData.do"
)

df = pd.read_csv('./criminal/crime.csv', encoding='CP949')
st.write(df)

