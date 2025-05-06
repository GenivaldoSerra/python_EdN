import streamlit as st

def main():
    st.set_page_config(
        page_title="Número Par ou Ímpar",
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
        .par {
            background-color: rgba(76, 175, 80, 0.2);
            border: 1px solid #4CAF50;
        }
        .impar {
            background-color: rgba(244, 67, 54, 0.2);
            border: 1px solid #f44336;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="title">🔢 Número Par ou Ímpar 🔢</h1>', unsafe_allow_html=True)

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

    col_btn1, col_btn2 = st.columns(2)
    
    with col_btn1:
        verificar_btn = st.button("Verificar", use_container_width=True, key="verificar_btn")

    with col_btn2:
        limpar_campos = st.button("Limpar Campos", use_container_width=True, key="limpar_campos_btn")
    
    if verificar_btn:
        if numero % 2 == 0:
            resultado = "O número é par."
            classe = "par"
        else:
            resultado = "O número é ímpar."
            classe = "impar"

        st.markdown(f'<div class="result-container {classe}">{resultado}</div>', unsafe_allow_html=True)
    
    if limpar_campos:
        st.session_state.limpar_campos = True
        st.rerun()

    st.markdown("<div class='footer'>© 2025 - Número Par ou Ímpar</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()