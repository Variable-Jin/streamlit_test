import streamlit as st
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv')
st.write(df)
5:07
pd.Series(model.coef_, index = X.columns)