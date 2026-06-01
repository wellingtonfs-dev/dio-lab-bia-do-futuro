import streamlit as st
import agente  # Importa o arquivo do agente de IA

# Interface Visual
st.title("Lume, Seu Educador Financeiro")

# Input do Chat
if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    # Exibe a mensagem do usuário na tela
    st.chat_message("user").write(pergunta)

    # Processa e exibe a resposta do assistente
    with st.spinner("Processando..."):
        resposta_lume = agente.perguntar(pergunta)
        st.chat_message("assistant").write(resposta_lume)