import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Perfil - JMS Obras", page_icon="👤")

st.header("👤 Cadastro de Usuário e Configurações")
st.markdown("Configure os dados da sua empresa para personalizar seus orçamentos.")

# Criar pasta assets se não existir para salvar o logo
if not os.path.exists("assets"):
    os.makedirs("assets")

# Formulário de Configurações
with st.form("perfil_form"):
    st.subheader("Dados da Empresa")
    nome_empresa = st.text_input("Nome do Profissional ou Empresa", placeholder="Ex: JMS Obras e Reformas")
    
    col1, col2 = st.columns(2)
    with col1:
        whatsapp = st.text_input("WhatsApp para Contato", placeholder="(31) 98888-7777")
    with col2:
        email = st.text_input("E-mail Profissional")
    
    endereco = st.text_input("Endereço/Cidade")
    
    st.markdown("---")
    st.subheader("Identidade Visual")
    upload_logo = st.file_uploader("Upload de Logotipo (PNG ou JPG)", type=["png", "jpg", "jpeg"])
    
    submit = st.form_submit_button("Salvar Configurações")

if submit:
    # Salvar dados na sessão para uso nos outros módulos
    st.session_state.perfil = {
        "nome": nome_empresa,
        "whatsapp": whatsapp,
        "email": email,
        "endereco": endereco
    }
    
    if upload_logo is not None:
        image = Image.open(upload_logo)
        image.save("assets/logo.png")
        st.success("Configurações e Logotipo salvos com sucesso!")
        st.image(image, caption="Logotipo Atual", width=150)
    else:
        st.success("Configurações salvas (sem alteração no logotipo).")

# Visualização do Perfil Atual
if 'perfil' in st.session_state:
    st.markdown("---")
    st.info(f"**Perfil Ativo:** {st.session_state.perfil['nome']} | {st.session_state.perfil['whatsapp']}")