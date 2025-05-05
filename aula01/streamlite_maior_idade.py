import streamlit as st
from datetime import datetime

def main():
    st.set_page_config(
        page_title="AVS - Age Verification System",
        page_icon="👋",
        layout="centered"
    )

    if "limpar_campos" in st.session_state and st.session_state.limpar_campos:
        st.session_state.nome = ""
        st.session_state.ano_nascimento = 2000
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

    st.markdown('<h1 class="title">AVS - Age Verification System</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        nome = st.text_input("Digite seu nome:", key="nome")
        ano_nascimento = st.number_input(
            "Digite o ano de nascimento:",
            min_value=1900,
            max_value=datetime.now().year,
            value=st.session_state.get("ano_nascimento", 2000),
            step=1,
            key="ano_nascimento"
        )

    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        verificar = st.button("Verificar Idade", use_container_width=True)

    with col_btn2:
        limpar = st.button("Limpar Campos", use_container_width=True)

    if verificar:
        if not nome.strip():
            st.error("Por favor, digite seu nome.")
        else:
            idade = datetime.now().year - ano_nascimento
            status = "maior" if idade >= 18 else "menor"

            st.markdown(f"""
            <div class='result-container {status}'>
                <h3>Resultado:</h3>
                <p>Olá <b>{nome}</b>, sua idade é <b>{idade} anos</b>.</p>
                <p>Você é <b>{status} de idade</b>.</p>
            </div>
            """, unsafe_allow_html=True)

    if limpar:
        st.session_state.limpar_campos = True
        st.rerun()

    st.markdown("<p class='footer'>© 2025 - AVS - Age Verification System</p>", unsafe_allow_html=True)

if __name__ == "__main__":

    if "nome" not in st.session_state:
        st.session_state.nome = ""
    if "ano_nascimento" not in st.session_state:
        st.session_state.ano_nascimento = 2000
    if "limpar_campos" not in st.session_state:
        st.session_state.limpar_campos = False

    main()