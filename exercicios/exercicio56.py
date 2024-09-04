# Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e utilize um laço while para exibir a mensagem a quantidade de vezes desejada

mensagem = (input('Digite a  mensagem que sera exibida: \n'))
quantidade = int(input('Digite a quantidade de vezes que a mensagem sera exibida: \n'))
val = 0

while val < quantidade:
    print(mensagem)
    val += 1
