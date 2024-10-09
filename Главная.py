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
    # st.write(tickerDf.columns)
    # st.write(tickerDf.reset_index().columns)

    new_df=tickerDf.reset_index()
    if 'Close' in new_df and 'Volume' in new_df and 'Date' in new_df:
            fig,ax=plt.subplots(figsize=(20,10))
            ax.plot(new_df['Date'], new_df['Close'], label='Цена закрытия')
            ax.set_xlabel('Дата')
            ax.set_ylabel('Цена')
            ax.set_title('График цен закрытия')
            ax.legend()
            for spine in ax.spines.values():
                spine.set_visible(False)
            ax.yaxis.grid(True)
            st.pyplot(fig)
        # st.line_chart(new_df['Volume'])
    else:
        st.error("Отсутствуют необходимые данные в DataFrame.")

with tabs[1]:
    tickerSymbol="AAPL"
    tickerData=yf.Ticker(tickerSymbol)
    st.title("Информация о компании")
    st.write(tickerData.info)


