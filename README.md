# Open High Open Low Strategy

This is a web app built using **Streamlit** that implements the **Open High Open Low** stock trading strategy. The app allows users to upload any stock data CSV file, filters out rows where the **Open price equals the High price** and **Open price equals the Low price**, and displays the results in a user-friendly format.

## Features

- Upload any stock data CSV file.
- Displays data where `OPEN = LOW` (Open High strategy).
- Displays data where `OPEN = HIGH` (Open Low strategy).
- Interactive and easy-to-use interface.

## How to Use

### Prerequisites

Ensure you have Python installed on your machine. If you don’t have Streamlit and pandas installed, use the following command to install them:

```bash
pip install streamlit pandas

Running the App Locally
Clone the repository or download the code.
Navigate to the directory containing app.py.
Start the app with the following command:

```bash
streamlit run app.py

The app will open in your default web browser, allowing you to upload a CSV file with stock data.
Alternatively, you can directly access the deployed app here:
[Open High Open Low Strategy](https://openhigh-or-low.streamlit.app/)

CSV File Format
Ensure that your CSV file has the following columns (case-insensitive):

OPEN: The opening price of the stock.
LOW: The lowest price of the stock.
HIGH: The highest price of the stock.
Example CSV Format

```arduino
SYMBOL,OPEN,LOW,HIGH
TCS,3500,3480,3520
INFY,1500,1490,1510
RELIANCE,2400,2380,2410

What the App Does
Open High: Displays rows where the OPEN price equals the LOW price.
Open Low: Displays rows where the OPEN price equals the HIGH price.

Screenshot

Technologies Used
Streamlit: For building the web app.
Pandas: For data manipulation and filtering.

