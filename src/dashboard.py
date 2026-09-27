import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Configuração da página
st.set_page_config(page_title="Dashboard IoT", layout="wide")

# Conexão com o banco PostgreSQL no Docker
engine = create_engine('postgresql+psycopg2://postgres:iot123@localhost:5432/iot_db')

# Função com cache para otimizar leitura
@st.cache_data
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Título do dashboard
st.title('🌡️ Dashboard de Temperaturas IoT')
st.markdown("Visualização de dados processados em pipeline IoT com PostgreSQL e Docker.")

col1, col2 = st.columns(2)

# Gráfico 1: Média de temperatura por dispositivo
with col1:
    st.header('Média de Temperatura por Dispositivo')
    df_avg_temp = load_data('avg_temp_por_dispositivo')
    fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp', labels={'device_id': 'Dispositivo', 'avg_temp': 'Média (°C)'})
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Contagem de leituras por hora
with col2:
    st.header('Leituras por Hora do Dia')
    df_leituras_hora = load_data('leituras_por_hora')
    fig2 = px.line(df_leituras_hora, x='hora', y='contagem', markers=True, labels={'hora': 'Hora', 'contagem': 'Total Leituras'})
    st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Temperaturas máximas e mínimas por dia
st.header('Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'], labels={'data': 'Data', 'value': 'Temperatura (°C)', 'variable': 'Métrica'})
st.plotly_chart(fig3, use_container_width=True)