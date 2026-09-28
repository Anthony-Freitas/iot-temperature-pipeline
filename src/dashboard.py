import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.set_page_config(page_title="Dashboard IoT", layout="wide")

DATABASE_URI = 'postgresql+psycopg2://postgres:iot123@localhost:5432/iot_db'
engine = create_engine(DATABASE_URI)

@st.cache_data
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

st.title('🌡️ Dashboard de Temperaturas IoT')
st.markdown("Análise de leituras de sensores IoT processadas via pipeline ETL.")

col1, col2 = st.columns(2)

with col1:
    st.header('Média de Temperatura por Dispositivo')
    df_avg_temp = load_data('avg_temp_por_dispositivo')
    fig1 = px.bar(
        df_avg_temp, 
        x='device_id', 
        y='avg_temp', 
        labels={'device_id': 'Dispositivo', 'avg_temp': 'Temp Média (°C)'},
        text_auto=True
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.header('Leituras por Hora do Dia')
    df_leituras_hora = load_data('leituras_por_hora')
    fig2 = px.line(
        df_leituras_hora, 
        x='hora', 
        y='contagem', 
        markers=True, 
        labels={'hora': 'Hora do Dia', 'contagem': 'Total de Leituras'}
    )
    st.plotly_chart(fig2, use_container_width=True)

st.header('Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
fig3 = px.line(
    df_temp_max_min, 
    x='data', 
    y=['temp_max', 'temp_min'], 
    labels={'data': 'Data', 'value': 'Temperatura (°C)', 'variable': 'Métrica'}
)
st.plotly_chart(fig3, use_container_width=True)