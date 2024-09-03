# Crie um programa que solicite ao usuário três números e exiba o maior deles

numero1 = int(input('Digite o primeiro: \n'))
numero2 = int(input('Digite o segundo numero: \n'))
numero3 = int(input('Digite o terceiro numero: \n'))

if numero1 > numero2 and numero1 > numero3:
    print(numero1)
elif numero2 > numero3:
    print(numero2)
else:
    print(numero3)
