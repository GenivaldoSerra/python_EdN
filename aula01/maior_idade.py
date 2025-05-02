# 1. Crie um programa que pergunte a idade de uma pessoa e diga se ela já é maior de idade ou não.

idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print(f"Sua idade é {idade}. Você é maior de idade.")
else:
    print(f"Sua idade é {idade}. Você é menor de idade.")