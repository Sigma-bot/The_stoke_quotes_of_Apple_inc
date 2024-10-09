import yfinance as yf
import streamlit as st
import pandas as pd
import datetime 
import matplotlib.pyplot as plt

tabs = st.tabs(["Главная", "О компании 'Яблоко'"])

with tabs[0]:
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

    # st.write(tickerDf.head(5))
    # fig,ax=plt.subplots(figsize=(100,100))
    # ax.plot(tickerDf['Index'],tickerDf['Close'])
    # st.pyplot(fig)

with tabs[1]:
    tickerSymbol="AAPL"
    tickerData=yf.Ticker(tickerSymbol)
    st.title("Информация о компании")
    st.write(tickerData.info)


