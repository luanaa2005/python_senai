# Crie um programa que peça ao usuário para inserir um número e, em seguida, exiba os números de 1 até esse número, mas de forma decrescente

numero = int(input('Informe um numero: \n'))

for i in range(numero):
    print(numero - i)

