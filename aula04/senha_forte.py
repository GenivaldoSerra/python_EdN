def validar_senha(senha):

    erros = []
    tem_numero = False
    tem_maiuscula = False
    tem_minuscula = False
    tem_especial = False
    caracteres_especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    for char in senha:
        if char.isdigit():
            tem_numero = True
        elif char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char in caracteres_especiais:
            tem_especial = True

    if len(senha) < 8:
        erros.append("A senha deve ter ao menos 8 caracteres.")
    if not tem_numero:
        erros.append("A senha deve conter ao menos um número.")
    if not tem_maiuscula:
        erros.append("A senha deve conter ao menos uma letra maiúscula.")
    if not tem_minuscula:
        erros.append("A senha deve conter ao menos uma letra minúscula.")
    if not tem_especial:
        erros.append("A senha deve conter ao menos um caractere especial (!@#$%^&* etc.).")

    return len(erros) == 0, erros

def main():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")

        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break

        valida, erros = validar_senha(senha)

        if valida:
            print("Senha validada com sucesso!")
            break
        else:
            print("Senha fraca! Corrija os seguintes problemas:")
            for erro in erros:
                print(f"- {erro}")

if __name__ == "__main__":
    main()