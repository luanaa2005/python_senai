# Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo

numero1 = int(input('digite o primeiro numero: \n'))
numero2 = int(input('digite o segundo numero: \n'))

while numero1 < numero2:
    numero1 = int(input('digite o primeiro numero: \n'))
    numero2 = int(input('digite o segundo numero: \n'))


