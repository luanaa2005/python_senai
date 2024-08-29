# Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a soma deles é maior que 100

numero1 = int(input('digite o primeiro numero: \n'))
numero2 = int(input('digite o segundo numero: \n'))

if numero1 + numero2 > 100:
    print('a soma entre os numeros eh maior que 100')
elif numero1 + numero2 < 100:
    print('a soma entre os numeor eh menor que 100')
else:
    print('a soma eh igual a 100')