# Escreva um programa que peça ao usuário para inserir dois números e verifique se o primeiro é maior que o segundo.

numero1 = int(input('digite o primeiro numero: \n'))
numero2 = int(input('digite o segundo numero: \n'))

if numero1 >  numero2:
    print('o primeiro numero eh maior que o segundo')
elif numero1 < numero2:
    print('o primeiro numero nao eh maior que o segundo')
else:
    print('os numeros sao iguais')