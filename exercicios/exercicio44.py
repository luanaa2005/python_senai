# Crie um programa que peça ao usuário 10 números e exiba apenas os números pares

numeros_pares = []

for pergunta in range(10):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)

print('Numeros pares: ', sorted(numeros_pares))
    

