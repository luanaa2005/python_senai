# Faça um programa que pergunte ao usuário a idade e verifique se ele pode votar (idade maior ou igual a 16

idade = int(input('Informe a idade: \n'))

if idade > 16 or idade == 16:
    print('pode votar')
else:
    print('nao pode votar')
