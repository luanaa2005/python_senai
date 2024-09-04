# Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.

numero_list = []
maior = 0

for i in range(5):
    numero = int(input('Digite um numero: '))
    numero_list.append(numero)
    if numero > maior:
        maior = numero

menor = maior
for numero in numero_list:
    if numero < menor:
        menor = numero

print('\nsua lista:', numero_list)
print('maior numero da lista:', maior)
print('menor numero da lista:', menor, '\n')
