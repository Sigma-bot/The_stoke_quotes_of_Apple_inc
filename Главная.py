import yfinance as yf
import streamlit as st
import pandas as pd
import datetime 
import matplotlib.pyplot as plt
import io

tabs = st.tabs(["Главная", "О компании 'Яблоко'"])

with tabs[0]:
    st.title("Элементарное приложение для оценки акций Apple")
    st.write("Графики интерактивные, ты можешь менять масштаб с помощью мышки.")
    st.write("Чтобы вернуть график в первоначальное положение используйте двойной клик")
    
    tickerSymbol = "AAPL"
    tickerData = yf.Ticker(tickerSymbol)

    start = st.sidebar.date_input("Выберите начало исследуемого периода", datetime.date(2010, 5, 31))
    end = st.sidebar.date_input("Выберите конец исследуемого периода", datetime.date(2020, 5, 31))

    tickerDf = tickerData.history(period='1d', start=start, end=end)

    if tickerDf.empty:
        st.write("Нет данных для выбранного периода.")
    else:
        st.write("## График цен закрытия")
        st.line_chart(tickerDf['Close'])

        st.write("## График объема торгов")
        st.line_chart(tickerDf['Volume'])

        new_df = tickerDf.reset_index()
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(new_df['Date'], new_df['Close'], label='Цена закрытия')
        ax.set_xlabel('Дата')
        ax.set_ylabel('Цена')
        ax.set_title('График цен закрытия')
        ax.legend()
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.yaxis.grid(True)

        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        st.sidebar.download_button("Скачать график закрытия цен", buf, "graph_close.png", "image/png")

        buf.seek(0)
        buf.truncate()

        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(new_df['Date'], new_df['Volume'], label='Объем торгов')
        ax.set_xlabel('Дата')
        ax.set_ylabel('Цена')
        ax.set_title('График объема торгов')
        ax.legend()
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.yaxis.grid(True)

        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        st.sidebar.download_button("Скачать график объема торгов", buf, "graph_volume.png", "image/png")

with tabs[1]:
    tickerData = yf.Ticker(tickerSymbol)
    st.subheader("Основная информация")
    st.write(f"**Название:** {tickerData.info['longName']}")
    st.write(f"**Сектор:** {tickerData.info['sector']}")
    st.write(f"**Отрасль:** {tickerData.info['industry']}")
    st.write(f"**Официальный сайт:** [Apple]({tickerData.info.get('website', 'Нет')})")
    st.write(f"**Количество сотрудников:** {tickerData.info['fullTimeEmployees']}")
    st.write(f"**Дата основания:** {tickerData.info.get('dateFounded', 'Нет информации')}")
    st.write(f"**Штаб-квартира:** {tickerData.info.get('address1', 'Нет информации')}, {tickerData.info.get('city', 'Нет информации')}, {tickerData.info.get('state', 'Нет информации')}, {tickerData.info.get('zip', 'Нет информации')}")
    st.write(f"**Рыночная капитализация:** ${tickerData.info.get('marketCap', 0):,}")
    st.write(f"**Цена акции:** ${tickerData.info.get('currentPrice', 0):.2f}")

