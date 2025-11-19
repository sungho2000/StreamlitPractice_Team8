import streamlit as st
import pandas as pd

#title
st.header("Task 2: 데이터 표시하기")
st.write("데이터프레임")

df= pd.read_csv("penguins.csv", encoding="utf-8")
st.dataframe(df)

#title
st.title('Task5: 파일 업로드')

uploaded_file = st.file_uploader("Upload Your data", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Uploaded Data")
    st.write(df)

