"""
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem.

    Parâmetros:
        valor_conta (float): O valor total da conta
        porcentagem_gorjeta (float): Porcentagem da gorjeta

    Retorna:
        float: O valor da gorjeta calculada
"""

def calcular_gorjeta():
    
    try:
        valor_conta = float(input("Digite o valor total da conta: "))
        if valor_conta < 0:
            print("O valor da conta não pode ser negativo.")
            return 0.0

        porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))
        if porcentagem_gorjeta < 0:
            print("A porcentagem da gorjeta não pode ser negativa.")
            return 0.0

        gorjeta = valor_conta * (porcentagem_gorjeta / 100)
        print(f"O valor da gorjeta é: R${gorjeta:.2f}")
        return gorjeta

    except ValueError:
        print("Entrada inválida. Por favor, digite valores numéricos.")
        return 0.0

if __name__ == "__main__":
    calcular_gorjeta()