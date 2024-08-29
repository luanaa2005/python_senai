# Desenvolva um algoritmo que peça ao usuário para digitar um número e verifique se ele é múltiplo de 2 ou de 5

numero = int(input('Digite um numero: \n'))

if numero % 2 == 0 and numero % 5 == 0:
    print('multiplo de 2 e 5')
elif numero % 2 == 0:
    print('multiplo de 2')
elif numero % 5 == 0:
    print('multiplo de 5')
else:
    print('nao eh multiplo de 2 nem 5')