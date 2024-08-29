# Faça um programa que peça ao usuário três números e verifique se todos são positivos

numero1 = float(input('digite o primeiro numero: \n'))
numero2 = float(input('digite o segundo numero: \n'))
numero3 = float(input('digite o terceiro numero: \n'))

if numero1 > 0 and numero2 > 0 and numero3 > 0:
    print('todos os numeros sao positivos')
elif numero1 < 0 and numero2 < 0 and numero3 < 0:
    print('nenhum numero eh positivo')
else:
    print('nem todos os numeros sao positivos')
