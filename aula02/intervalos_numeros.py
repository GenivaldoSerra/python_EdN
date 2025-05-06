import streamlit as st

def main():
    st.set_page_config(
       page_title="Intervalos Numéricos",
       page_icon="🔢",
       layout="centered" 
    )

    if "limpar_campos" in st.session_state and st.session_state.limpar_campos:
        st.session_state.numero = 0
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
        .intervalo {
            background-color: rgba(76, 175, 80, 0.2);
            border: 1px solid #4CAF50;
        }
        .fora_intervalo {
            background-color: rgba(244, 67, 54, 0.2);
            border: 1px solid #f44336;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="title">🔢 Intervalos Numéricos 🔢</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        numero = st.number_input(
            "Digite um número:",
            min_value=0,
            max_value=1000000,
            value=st.session_state.get("numero", 0),
            step=1,
            key="numero"
        )

        inicial = st.number_input(
            "Digite um número para iniciar o intervalo:",
            min_value=0,
            max_value=1000000,
            value=st.session_state.get("inicial", 1),
            step=1,
            key="inicial"
        )

        final = st.number_input(
            "Digite um número para o final do intervalo:",
            min_value=0,
            max_value=1000000,
            value=st.session_state.get("final", 1000),
            step=1,
            key="final"
        )

    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        verificar_btn = st.button("Verificar", use_container_width=True, key="verificar_btn")
    
    with col_btn2:
        limpar_btn = st.button("Limpar Campos", use_container_width=True, key="limpar_btn")

    if verificar_btn:
        if numero == 0:
            st.error("O número deve ser maior que 0.", icon="🚨")
            if inicial >= final:
                st.error("O número inicial deve ser menor que o número final.", icon="🚨")
            elif inicial <= numero <= final:
                st.success(f"O número {numero} está dentro do intervalo [{inicial}, {final}].", icon="✅")
            
            st.markdown(f"""
                <div class="result-container intervalo">
                    <p>O número {numero} está dentro do intervalo [{inicial}, {final}]</p>
                </div>
            """, unsafe_allow_html=True)

    if limpar_btn:
        st.session_state.limpar_campos = True
        st.rerun()
    
    st.markdown("<div class='footer'>© 2025 - Intervalos Numéricos</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()