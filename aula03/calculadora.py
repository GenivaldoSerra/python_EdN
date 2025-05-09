from unittest import result


def calculadora():
    """
    Realiza operações matemáticas básicas com dois números inseridos pelo usuário.
    """

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            break  # Sai do loop se a conversão para float for bem-sucedida
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

    while True:
        operacao = input("Digite a operação desejada (+, -, *, /): ")
        if operacao in ("+", "-", "*", "/"):
            break  # Sai do loop se a operação for válida
        else:
            print("Operação inválida. Por favor, escolha entre +, -, *, /.")

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 == 0:
            resultado = "Erro: Divisão por zero!"
        else:
            resultado = num1 / num2

    print("Resultado:", resultado)

if __name__ == "__main__":
    calculadora()
