import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Precios de Acciones APP

Precios de cierres y volumen para acciones
""")

st.sidebar.text_input("Escriba el Ticker de la acción", key="ticker")
fechas = st.sidebar.date_input("Rango de fechas",[])


if st.session_state.ticker == "":
   accion = "GOOGL" 
else:
   accion = st.session_state.ticker

data = yf.Ticker(accion)

accionDF = data.history(period='1d', start='2021-01-01', end='2021-08-01')
st.wrte(fechas)
st.line_chart(accionDF.Close)
st.line_chart(accionDF.Volume)

st.dataframe(accionDF)

