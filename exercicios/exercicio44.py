# Crie um programa que peça ao usuário 10 números e exiba apenas os números pares

numero_list = []

for pergunta in range(10):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        numero_list.append(numero)

print('Numeros pares: ' , numero_list)
    

