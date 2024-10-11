import pandas as pd
import plotly.express as px
import streamlit as st 
car_data = pd.read_csv("vehicles_us.csv")
st.header('Proyecto 6 - Datos sobre autos')
build_histogram = st.checkbox('Construir histograma') # crear un botón
        
if build_histogram: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer",
                               color_discrete_sequence=['darkblue'])
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)
            fig.update_layout(
    title_text='Kilometraje de los coches en venta y su frecuencia', # title of plot
    xaxis_title_text='Odómetro', # xaxis label
    yaxis_title_text='Frecuencia', # yaxis label
    
)
build_scatter = st.checkbox('Construir gráfico de dispersión') # crear un botón
     
if build_scatter: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.scatter(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)