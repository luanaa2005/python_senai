#  Escreva um programa que solicite ao usuário para inserir 3 nomes e armazene-os em uma lista. Em seguida, imprima a lista completa

nome1 = (input('Insira o primeiro nome: \n'))
nome2 = (input('Insira o segundo nome: \n'))
nome3 = (input('Insira o terceiro nome: \n'))

nomes = [nome1, nome2, nome3]

print('\nlista de nomes: ')
for i in nomes:
    print(i)


