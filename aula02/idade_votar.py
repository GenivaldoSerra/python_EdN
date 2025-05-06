import streamlit as st

from datetime import datetime


def main():
    st.set_page_config(
        page_title="Idade para Votar",
        page_icon="🗳️",
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

    st.markdown('<h1 class="title">🗳️ Idade para Votar 🗳️</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        nome = st.text_input("Digite seu nome:", key="nome")
        ano_nascimento = st.number_input(
            "Digite o ano de nascimento:",
            min_value=1900,
            max_value=datetime.now().year,
            value=st.session_state.get("ano_nascimento", 1900),
            step=1,
            key="ano_nascimento"
        )

    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        verificar_btn = st.button("Verificar", use_container_width=True, key="verificar_btn")
    
    with col_btn2:
        limpar_campos_btn = st.button("Limpar Campos", use_container_width=True, key="limpar_campos_btn")

    if verificar_btn:
        if not nome:
            st.error("Por favor, digite seu nome.")
        else:
            idade = datetime.now().year - ano_nascimento
            if idade >= 16:
                st.success(f"Olá {nome}, sua idade é {idade} anos, você pode votar! 🎉")
            else:
                st.error(f"Olá {nome}, você ainda não pode votar. Você tem apenas {idade} anos.")

    st.markdown('<div class="footer">Desenvolvido por [Seu Nome]</div>', unsafe_allow_html=True)

    if limpar_campos_btn:
        st.session_state.limpar_campos = True
        st.rerun()

if __name__ == "__main__":
    main()