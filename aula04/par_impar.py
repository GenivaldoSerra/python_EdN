# Aula 04
# Contador de números Par ou Impar

def main():

    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número (ou 'fim' para encerrar): ")

        if entrada.lower() == 'fim':
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"O número {numero} é par. ")
                pares += 1
            else:
                print(f"O número {numero} é impar. ")
                impares += 1
        except ValueError:
            print("Digite um número válido, ou digite 'fim'.")
        
    print("\nResultado: ")
    print(f"O total de números pares é: {pares}")
    print(f"O total de números impares é: {impares}\n")

if __name__ == "__main__":
    main()