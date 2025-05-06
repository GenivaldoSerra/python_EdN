import streamlit as st
from datetime import datetime

def main():
    st.set_page_config(
        page_title="Validador de Dia Útil",
        page_icon="📅",
        layout="centered"
    )

    if "limpar_campos" in st.session_state and st.session_state.limpar_campos:
        st.session_state.data = datetime.now().date()
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
    .util {
        background-color: rgba(76, 175, 80, 0.2);
        border: 1px solid #4CAF50;
    }
    .nao_util {
        background-color: rgba(244, 67, 54, 0.2);
        border: 1px solid #f44336;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="title">📅 Validador de Dia Útil 📅</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        data = st.date_input(
            "Selecione uma data:",
            value=st.session_state.get("data", datetime.now().date()),
            key="data"
        )
        
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        verificar_btn = st.button("Verificar", use_container_width=True, key="verificar_btn")

    if verificar_btn:
        dia_util = data.weekday() < 5
        if dia_util:
            st.markdown(f'<div class="result-container util">O dia {data} é um dia útil.</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="result-container nao_util">O dia {data} não é um dia útil.</div>', unsafe_allow_html=True)
    

    st.markdown('<footer class="footer">© 2025 - Validador de Dia Útil</footer>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()