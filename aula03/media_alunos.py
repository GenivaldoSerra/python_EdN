# Registrar notas dos alunos

def media():
    notas = []
    numero_de_alunos = 0

    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
        
        if entrada.lower() == 'fim':
            break
        
        try:
            nota = float(entrada)

            if 0 <= nota <= 10:
                notas.append(nota)
                numero_de_alunos += 1
            else:
                print("Nota inválida. Digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número válido, ou digite 'fim'.")
        
    # Calculo da média
    if numero_de_alunos > 0:
        media = sum(notas) / numero_de_alunos
        print(f"A média das notas é: {media:.2f}")
        print(f"O total de alunos é: {numero_de_alunos}")
    
    else:
        print("Nenhuma nota registrada.")

if __name__ == "__main__":
    media()