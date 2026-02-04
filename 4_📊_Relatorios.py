import streamlit as st
import pandas as pd

st.set_page_config(page_title="Relatórios - JMS Obras", page_icon="📊")

st.header("📊 Relatórios e Dashboard")

# Simulação de dados para visualização (Métricas solicitadas)
data = {
    'Status': ['Aprovados', 'Pendentes', 'Aprovados', 'Aprovados', 'Pendentes'],
    'Valor': [2500, 1200, 3000, 4500, 800],
    'Serviço': ['Pintura', 'Piso', 'Alvenaria', 'Pintura', 'Piso']
}
df = pd.DataFrame(data)

# Layout de Colunas para Métricas [cite: 26]
col1, col2, col3 = st.columns(3)

with col1:
    total_orcado = df['Valor'].sum()
    st.metric("Total Orçado (Mês)", f"R$ {total_orcado:,.2f}") [cite: 25]

with col2:
    ticket_medio = df['Valor'].mean()
    st.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}") [cite: 26]

with col3:
    aprovados = len(df[df['Status'] == 'Aprovados'])
    st.metric("Orçamentos Aprovados", aprovados) [cite: 24]

st.markdown("---")

# Gráficos de Performance [cite: 24]
st.subheader("Visualização de Performance")
col_graph1, col_graph2 = st.columns(2)

with col_graph1:
    st.write("Status de Orçamentos")
    st.bar_chart(df['Status'].value_counts()) [cite: 24]

with col_graph2:
    st.write("Serviços mais Solicitados")
    st.bar_chart(df['Serviço'].value_counts()) [cite: 26]

st.info("💡 Dica: No futuro, estes dados serão lidos automaticamente do seu banco de dados de orçamentos.")