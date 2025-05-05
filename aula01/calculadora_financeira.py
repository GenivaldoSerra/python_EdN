import streamlit as st


def main():
    st.set_page_config(page_title="Calculadora Financeira", page_icon="💸")

    st.title("💸 Calculadora Financeira 💸")

    produto = st.text_input("Digite o nome do produto: ", key="produto")
    preco_original = st.number_input(
        "Digite o preço do produto (R$): ", 
        min_value=0.0, 
        key="preco", 
        format="%.2f", 
        step=0.01
    )
    desconto = st.slider(
        "Desconto (R$)",
        min_value=0,
        max_value=100,
        value=10,
        key="desconto",
    )

    if st.button("Calcular"):
        if not produto:
            st.warning("Por favor, digite o nome do produto.")
        else:
            valor_desconto = preco_original * (desconto / 100)
            preco_final = preco_original - valor_desconto

            st.markdown(f"""
                ### Resultado:
                - Produto: **{produto}**
                - Preço Orginal: **R$ {preco_original:.2f}**
                - Desconto de {desconto}%: **R$ {valor_desconto:.2f}**
                - Preço com desconto: **R$ {preco_final:.2f}**
            """)
    
    st.markdown("---")
    st.caption("© 2025 - Calculadora Financeira")

if __name__ == "__main__":
    main()