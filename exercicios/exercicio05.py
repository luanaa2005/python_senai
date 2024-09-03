# Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.

numero1 = float(input('Digite um numero: \n'))
numero2 = float(input('Digite outro nummero: \n'))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print('ambos sao pares')
else:
    print('algum numero ou ambos numeros nao sao pares')
    