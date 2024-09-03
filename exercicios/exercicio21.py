# Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10

numero = float(input('insira um numero: \n'))

if numero > 10:
    print('maior que 10')
elif numero < 10:
    print('menor que 10')
else:
    print('igual a 10')
