import streamlit as st

from datetime import datetime

def main():
    st.set_page_config(
        page_title="Classificação Etária",
        page_icon="👶",
        layout="centered"
    )

    if "limpar_campos" in st.session_state and st.session_state.limpar_campos:
        st.session_state.nome = ""
        st.session_state.ano_nascimento = 1900
        st.session_state.limpar_campos = False
    
    st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 2rem;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 0.8rem;
        margin-top: 3rem;
    }
    .result-container {
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 2rem;
    }
    .maior {
        background-color: rgba(76, 175, 80, 0.2);
        border: 1px solid #4CAF50;
    }
    .menor {
        background-color: rgba(244, 67, 54, 0.2);
        border: 1px solid #f44336;
    }
    </style>
    """, unsafe_allow_html=True)