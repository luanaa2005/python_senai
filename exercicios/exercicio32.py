# Escreva um programa que solicite ao usuário uma palavra e verifique se ela é um palíndromo (lê-se igual de trás para frente)

palindromo = input('Digite uma palavra: \n')

if palindromo.lower() == palindromo[::-1].lower():
    print('é palindromo')
else:
    print('nao é palindromo')
