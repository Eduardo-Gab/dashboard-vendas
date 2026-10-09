import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.set_page_config(page_title='Dashboard de Vendas', layout='wide')

engine = create_engine('sqlite:///database/vendas.db')
df = pd.read_sql('SELECT * FROM vendas', engine, parse_dates=['data'])

st.title('Dashboard de Vendas')

regiao_filtro = st.sidebar.multiselect('Regiao', df['regiao'].unique(), default=df['regiao'].unique())
df_filtrado = df[df['regiao'].isin(regiao_filtro)]

col1, col2, col3 = st.columns(3)
col1.metric('Faturamento Total', f"R$ {df_filtrado['valor_total'].sum():,.2f}")
col2.metric('Qtd. Vendida', int(df_filtrado['quantidade'].sum()))
col3.metric('Ticket Medio', f"R$ {df_filtrado['valor_total'].mean():,.2f}")

fig1 = px.bar(df_filtrado.groupby('produto')['valor_total'].sum().reset_index(), x='produto', y='valor_total', title='Faturamento por Produto')
st.plotly_chart(fig1, use_container_width=True)

df_temporal = df_filtrado.groupby(df_filtrado['data'].dt.to_period('M'))['valor_total'].sum().reset_index()
df_temporal['data'] = df_temporal['data'].astype(str)
fig2 = px.line(df_temporal, x='data', y='valor_total', title='Evolucao de Vendas por Mes')
st.plotly_chart(fig2, use_container_width=True)
