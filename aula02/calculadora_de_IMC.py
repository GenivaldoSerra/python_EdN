import streamlit as st


def main():
    st.set_page_config(
        page_title="Calculadora de IMC",
        page_icon="🏋️‍♂️",
        layout="centered"
    )

    if "limpar_campos" in st.session_state and st.session_state.limpar_campos:
        st.session_state.nome = ""
        st.session_state.peso = 0.0
        st.session_state.altura = 0.0
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
        .resultado {
            font-size: 1.5rem;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="title">Calculadora de IMC</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        nome = st.text_input("Digite seu nome:", key="nome")
        peso = st.number_input(
            "Digite seu peso(Kg):",
            min_value=0.0,
            max_value=300.0,
            value=st.session_state.get("peso", 0.0),
            step=0.1,
            key="peso"
        )
        altura = st.number_input(
            "Digite sua altura(m):",
            min_value=0.0,
            max_value=3.0,
            value=st.session_state.get("altura", 0.0),
            step=0.01,
            key="altura"
        )

    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        calcular = st.button("Calcular IMC", key="calcular")
    
    with col_btn2:
        limpar = st.button("Limpar Campos", key="limpar")
    
    if calcular:
        if not nome:
            st.warning("Por favor, insira seu nome.")
        elif  peso > 0 and altura > 0:
            imc = peso / (altura **2)
            
            st.markdown(f"""
                <div class="result-container"><p class="resultado">Olá {nome}, seu IMC é: {imc:.2f}</p></div>
            """, unsafe_allow_html=True)

            if imc < 18.5:
                st.success("Você está abaixo do peso.")
            elif 18.5 <= imc < 24.9:
                st.success("Você está com o peso normal.")
            elif 25 <= imc < 29.9:
                st.warning("Você está com sobrepeso.")
            else:
                st.error("Você está obeso.")
        else:
            st.warning("Por favor, insira valores válidos para peso e altura.")
    if limpar:
        st.session_state.limpar_campos = True
        st.rerun()
    
    st.markdown("<p class='footer'>© 2025 - Calculadora de IMC</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    if "nome" not in st.session_state:
        st.session_state.nome = ""
    if "peso" not in st.session_state:
        st.session_state.peso = 0.0
    if "altura" not in st.session_state:
        st.session_state.altura = 0.0
    if "limpar_campos" not in st.session_state:
        st.session_state.limpar_campos = False
    main()
