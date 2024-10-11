import pandas as pd
import plotly.express as px
import streamlit as st 
car_data = pd.read_csv("vehicles_us.csv")
st.header('Lanzar una moneda')
build_histogram = st.checkbox('Proyecto 6 - Datos sobre autos') # crear un botón
        
if build_histogram: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir gráfico de dispersión') # crear un botón
     
if build_scatter: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.scatter(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)