# Escreva um programa que peça ao usuário para inserir uma palavra e verifique se ela tem mais de 5 letras

palavra = str(input('Insira uma palavra: \n'))

if len(palavra) > 5:
    print('a palavra tem mais de 5 letras')
elif len(palavra) < 5:
    print('a palavra tem menos de 5 letras')
else:
    print('a palavra tem 5 letras')
