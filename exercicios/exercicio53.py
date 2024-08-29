# Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1

numero = int(input('Informe um numero: \n'))

for i in range(numero):
    print(numero - i)