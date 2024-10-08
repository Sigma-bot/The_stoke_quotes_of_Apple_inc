import yfinance as yf
import streamlit as st


tickerSymbol="AAPL"
tickerData=yf.Ticker(tickerSymbol)
st.title("Информация о компании")
st.write(tickerData.info)