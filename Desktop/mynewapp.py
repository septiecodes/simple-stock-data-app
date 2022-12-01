import streamlit as st 
import yfinance as yf 
import pandas as pd

st.write("""

# Data-driven Stock Price App
The stock closing price and volume of Microsoft!

""")

tickerSymbol = "MSFT"

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period="1d", start="2012-1-12", end="2022-1-12")

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

