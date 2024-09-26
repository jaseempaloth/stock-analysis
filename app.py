import streamlit as st
import pandas as pd

st.title("Open High Open Low Strategy")

uploaded_file = st.file_uploader('Upload your csv file', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()

    # Remove columns that have all null values
    df = df.dropna(axis=1, how='all')

    open_high = df[df['OPEN'] == df['LOW']]
    open_low = df[df['OPEN'] == df['HIGH']]

    st.subheader("Open High")
    st.dataframe(open_high)

    st.subheader("Open Low")
    st.dataframe(open_low)

else:
    st.subheader("Please upload your csv file to proceed")
