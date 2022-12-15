import streamlit as st
import pandas as pandas

df = pd.read_csv('https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv')
st.write(df)

import joblib
model = joblib.load('./ml_model/app.py')
model_info = pd.Series(model_from_joblib.coef_, index = X.columns)
st.write(model_info)
