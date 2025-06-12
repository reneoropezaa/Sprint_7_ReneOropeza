import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')

df= load_data()

st.header("Exploracion de datos de vehiculos en EE.UU.")

hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creacion de un histograma para el edometro')
    fig= px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_buttom = st.button('Construir grafico de dispersion')

if scatter_buttom:
    st.write('Creacion de un grafico de dispersion entre edometro y precio')
    fig2= px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)