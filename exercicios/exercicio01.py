# Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").

numero = int(input('digite um numero de 1 a 3: \n'))

if numero == 1:
    print('um')
elif numero == 2:
    print('dois')
else:
    print('tres')
