import streamlit as st
import pandas as pd
import altair as alt

st.title("Open High Open Low Strategy")

# short description about the strategy
st.write("""
The **Open High Low strategy** is a trading method where:
- **Open High** refers to when the opening price(OPEN) of a stock is the same as its lowest price(LOW) of the day.
- **Open Low** refers to when the opening price(OPEN) of a stock is the same as its highest price(HIGH) of the day.
Traders use these patterns to identify potential price movements.
""")

uploaded_file = st.file_uploader('Upload your csv file', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()

    # Replace '-' or any non-null placeholder with NaN
    df.replace('-', pd.NA, inplace=True)

    # Then drop columns where all values are NaN
    df = df.dropna(axis=1, how='all')

    open_high = df[df['OPEN'] == df['LOW']]
    open_low = df[df['OPEN'] == df['HIGH']]

    st.subheader("Open High")
    st.dataframe(open_high)

    # Download filtered data as CSV
    st.download_button(
        label="Download Open High Data",
        data=open_high.to_csv(index=False),
        file_name='open_high.csv',
        mime='text/csv'
    )

    st.subheader("Open Low")
    st.dataframe(open_low)

    st.download_button(
        label="Download Open Low Data",
        data=open_low.to_csv(index=False),
        file_name='open_low.csv',
        mime='text/csv'
    )

    # User-defined threshold for % change
    user_threshold = st.slider("Change the Percentage", min_value=-5.0, max_value=10.0, value=1.0, step=0.1)
    
    # Filter data based on user input
    filtered_by_threshold = df[df['%CHNG'] >= user_threshold]
    st.subheader(f"Stocks with Price Change > {user_threshold}%")
    st.dataframe(filtered_by_threshold)


else:
    st.subheader("Please upload your csv file to proceed")

