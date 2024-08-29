# Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e depois use um for para imprimir essa mensagem repetidas vezes

mensagem = input('Qual mensagem deve ser exibida?: \n')
vezes = int(input('Quantas vezes a mensagem deve ser exibida?: \n'))

for i in range(vezes):
    print(mensagem)
