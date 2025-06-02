import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Análisis de anuncios de coches 🚗')

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para mostrar histograma
if st.button('Mostrar histograma del odómetro'):
    st.write('Histograma de millas recorridas')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón para mostrar gráfico de dispersión
if st.button('Mostrar dispersión precio vs odómetro'):
    st.write('Relación entre precio y millas recorridas')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)
