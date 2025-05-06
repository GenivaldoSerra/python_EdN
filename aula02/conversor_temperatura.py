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

