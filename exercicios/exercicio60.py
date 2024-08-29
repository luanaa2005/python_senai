# Crie um programa que peça ao usuário um número e exiba todos os divisores desse número.

numero = int(input('digite um numero: \n'))

print('divisores do numero: \n')

for i in range(numero, 0, -1):
    if numero % i == 0:
        print(i, end=' ')