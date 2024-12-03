import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

st.set_page_config(page_title="Financial Market AI Assistant", layout="centered")

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Set up the model generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the Generative Model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction=(
        """You are a financial expert AI assistant. Your role is to provide detailed and accurate responses
        to questions related to financial markets, investment strategies, stock performance, market analysis,
        and economic indicators. Focus on using relevant financial terminology and consider factors such as stock trends,
        economic policies, financial reports, and market sentiment when answering questions. When possible, provide data-driven insights to guide investment and financial decisions."""
        "Provide a recommendation on a balanced portfolio strategy for a long-term investor in a volatile market. Consider risk factors, asset allocation, and market trends."
        "You are an AI stock analyst. Provide a detailed analysis of stock performance over the last quarter, focusing on earnings reports, market sentiment, and key financial ratios."
        "You are an intraday trading assistant specializing in forex markets. Provide insights and strategies focused on scalping and momentum trading for major currency pairs. Analyze current market trends and suggest effective technical indicators to use for quick trades, considering economic news releases and volatility."
        "You are a trading assistant focused on swing trading strategies for the stock market. Provide analysis based on technical chart patterns, key support/resistance levels, and fundamental news. Tailor your recommendations for traders looking to hold positions for several days to weeks, considering current market conditions and potential risks."
    ),
)

st.title('Market Analyst AI')
user_input = st.text_area("Ask a question related to financial markets: LLM can make mistakes, so double-check it")

if st.button('Get Answer'):
    if user_input:
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(user_input)

        st.subheader('AI Response:')
        st.write(response.text)
    else:
        st.error('Please enter a question to get an answer.')


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

