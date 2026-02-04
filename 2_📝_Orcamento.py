import streamlit as st
from fpdf import FPDF
import pandas as pd

st.set_page_config(page_title="Orçamento - JMS Obras", page_icon="📝")

st.header("📝 Novo Orçamento")

# Dados do Cliente
with st.expander("👤 Dados do Cliente", expanded=True):
    cliente = st.text_input("Nome do Cliente")
    contato = st.text_input("Telefone/WhatsApp (com DDD)")
    descricao_obra = st.text_area("Descrição Geral do Serviço") [cite: 15]

# Integração com a Medição (Memória de Cálculo)
st.subheader("📋 Itens do Orçamento")
if 'memoria_calculo' in st.session_state and st.session_state.memoria_calculo:
    df_itens = pd.DataFrame(st.session_state.memoria_calculo)
    st.dataframe(df_itens, use_container_width=True)
    total_m2 = df_itens["Área (m²)"].sum()
    
    valor_unitario = st.number_input("Valor por m² (R$)", min_value=0.0, value=50.0)
    total_financeiro = total_m2 * valor_unitario
    st.metric("Total do Orçamento", f"R$ {total_financeiro:,.2f}") [cite: 21]
else:
    st.warning("Nenhuma medição encontrada. Vá até a aba 'Medição' para adicionar áreas.")

# Funções de Exportação
def gerar_pdf(cliente, total, itens):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Orçamento - JMS Obras", ln=True, align='C')
    
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, f"Cliente: {cliente}", ln=True)
    pdf.cell(200, 10, f"Valor Total: R$ {total:,.2f}", ln=True)
    pdf.ln(5)
    
    pdf.cell(200, 10, "Detalhes das Medições:", ln=True)
    for item in itens:
        pdf.cell(200, 10, f"- {item['Ambiente']}: {item['Área (m²)']} m² ({item['Tipo']})", ln=True)
    
    return pdf.output(dest='S').encode('latin-1')

# Ações
col1, col2 = st.columns(2)

with col1:
    if st.button("📄 Gerar PDF Personalizado") and cliente: [cite: 17]
        pdf_bytes = gerar_pdf(cliente, total_financeiro, st.session_state.memoria_calculo)
        st.download_button(label="Baixar Orçamento", data=pdf_bytes, file_name=f"Orcamento_{cliente}.pdf", mime="application/pdf")

with col2:
    if st.button("📲 Enviar via WhatsApp"): [cite: 18]
        msg = f"Olá {cliente}, o seu orçamento totalizou R$ {total_financeiro:,.2f}. Podemos agendar?"
        link_wa = f"https://wa.me/55{contato}?text={msg.replace(' ', '%20')}"
        st.markdown(f"[Clique aqui para enviar]({link_wa})") [cite: 18]