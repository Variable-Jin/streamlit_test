import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write(
   "https://www.data.go.kr/data/15081069/fileData.do"
)
df = pd.read_csv('./subway/ssubway.csv', encoding='CP949')
st.write(df)

fig = plt.figure(figsize=(10,7))
sns.histplot(data=df, x='호선', hue='조사일자', multiple='stack')
st.pyplot(fig)

sns.displot(data=df, x='호선', kind='kde')

