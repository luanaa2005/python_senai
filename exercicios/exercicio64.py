#  Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3


numero_list = []
for i in range(10):
    numero = int(input('Digite um numero aleatorio: '))
    if numero % 3 == 0:
        numero_list.append(numero)

print('\nnumeros multiplos de 3 na lista: ', numero_list)