import streamlit as st

st.set_page_config(page_title="Medição - JMS Obras", page_icon="📏")

st.header("📏 Calculadora de Medição")
st.markdown("Calcule áreas ($m^2$) para pintura, piso ou alvenaria em tempo real. ")

# Inicializa a memória de cálculo na sessão do navegador
if 'memoria_calculo' not in st.session_state:
    st.session_state.memoria_calculo = []

# Formulário de entrada
with st.form("form_medicao"):
    col1, col2 = st.columns(2)
    with col1:
        comodo = st.text_input("Nome do Ambiente (ex: Quarto 1)", placeholder="Parede A") [cite: 20]
    with col2:
        tipo_obra = st.selectbox("Tipo de Serviço", ["Pintura", "Piso/Revestimento", "Alvenaria"]) [cite: 21]

    col3, col4 = st.columns(2)
    with col3:
        largura = st.number_input("Largura ou Comprimento (m)", min_value=0.0, step=0.01) [cite: 20]
    with col4:
        altura = st.number_input("Altura ou Largura 2 (m)", min_value=0.0, step=0.01) [cite: 20]

    submit = st.form_submit_button("Adicionar à Memória de Cálculo") [cite: 22]

# Lógica para adicionar os dados
if submit:
    if largura > 0 and altura > 0 and comodo:
        area_total = largura * altura
        st.session_state.memoria_calculo.append({
            "Ambiente": comodo,
            "Tipo": tipo_obra,
            "Medidas": f"{largura}m x {altura}m",
            "Área (m²)": area_total
        })
        st.success(f"✅ {comodo} adicionado com sucesso!")
    else:
        st.error("Preencha todos os campos corretamente.")

# Exibição da Memória de Cálculo
if st.session_state.memoria_calculo:
    st.markdown("---")
    st.subheader("📋 Memória de Cálculo Atual") [cite: 22]
    
    df_medicoes = st.session_state.memoria_calculo
    st.table(df_medicoes)
    
    total_m2 = sum(item["Área (m²)"] for item in df_medicoes)
    st.info(f"**Área Total Acumulada: {total_m2:.2f} m²**") [cite: 21]

    if st.button("Limpar Medições"):
        st.session_state.memoria_calculo = []
        st.rerun()