import yfinance as yf
import streamlit as st
import pandas as pd
import datetime 
import pydeck as pdk

tabs = st.tabs(["Вкладка 1", "Вкладка 2"])

with tabs[0]:
    st.header("Содержимое Вкладки 1")
    st.write("Здесь может быть любой контент для первой вкладки.")

with tabs[1]:
    st.header("Содержимое Вкладки 2")
    st.write("Здесь может быть любой контент для второй вкладки.")

st.title("Элементарное приложение для оценки акций Apple")
st.write("Графики интерактивные, ты можешь менять масштаб с помощью мышки.")
st.write("Чтобы вернуть график в первоначальное положение используйте двойной клик")
tickerSymbol="AAPL"

tickerData=yf.Ticker(tickerSymbol)

start = st.sidebar.date_input("Выберите начало исследуемого периода", datetime.date(2010, 5, 31))
end = st.sidebar.date_input("Выберите начало исследуемого периода", datetime.date(2020, 5, 31))

tickerDf=tickerData.history(period='1d', start=start, end=end)

st.write("## График цен закрытия")
st.line_chart(tickerDf['Close'])

st.write("## График объема торгов")
st.line_chart(tickerDf['Volume'])
