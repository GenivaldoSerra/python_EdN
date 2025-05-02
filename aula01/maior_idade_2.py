# 1. Crie um programa que pergunte a idade de uma pessoa e diga se ela já é maior de idade ou não.

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print(f"Olá {nome}, sua idade é {idade} anos. Você é maior de idade.")
else:
    print(f"Olá {nome}, sua idade é {idade} anos. Você é menor de idade.")