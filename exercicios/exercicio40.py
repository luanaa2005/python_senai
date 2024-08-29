# Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais

numero1 = int(input('digite o primeiro numero: \n'))
numero2 = int(input('digite o segundo numero: \n'))
numero3 = int(input('digite o terceiro numero: \n'))

if numero1 == numero2 and numero2 == numero3:
    print('os numeros sao iguais')
else:
    print('os numeros sao diferentes')
