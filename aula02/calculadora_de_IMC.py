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

    


if __name__ == "__main__":
    main()
