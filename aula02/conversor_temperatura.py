import streamlit as st

def mai():
    st.set_page_config(
        page_title="Conversor de Temperatura",
        page_icon="🌡️",
        layout="centered"
    )
    

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
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="title"> 🌡️ Conversor de Temperatura 🌡️</h1>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        celsius = st.number_input(
            "Digite a temperatura em Celsius:",
            value=0.0,
            step=0.1,
            key="celsius"
        )

        col_btn1, col_btn2 = st.columns(2)

        with col_btn1:
            calcular = st.button("Converter", key="converter")
        
        with col_btn2:
            limpar = st.button("Limpar Campos", key="limpar_campos")
        
        if calcular:
            if not celsius:
                st.error("Por favor, insira um valor de temperatura.")
            else:
                fahrenheit = (celsius * 9/5) + 32
                kelvin = celsius + 273.15

                st.markdown(f"""
                <div class="result-container">
                    <h2>Resultados:</h2>
                    <p><strong>Fahrenheit:</strong> {fahrenheit:.2f} °F</p>
                    <p><strong>Kelvin:</strong> {kelvin:.2f} K</p>
                </div>
                """, unsafe_allow_html=True)
        
        if limpar:
            st.session_state.limpar_campos = True
            st.rerun()

        st.markdown("<p class='footer'>© 2025 - Conversor de Temperatura</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    if "celsius" not in st.session_state:
         st.session_state.celsius = 0.0
    if "limpar_campos" not in st.session_state:
        st.session_state.limpar_campos = False
    mai()