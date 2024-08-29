# Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 17 anos).

idade = int(input('Digite sua idade: \n'))

if idade >= 13 and idade <= 17:
     print('adolescente')
else:
    print('nao eh adolescente')