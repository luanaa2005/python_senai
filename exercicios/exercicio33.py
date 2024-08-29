# Crie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10%

valor = int(input('Informe o valor do produto: \n'))

print('valor do desconto:', valor * 10 / 100)
print('valor do produto com desconto: ', valor - valor * 10 / 100 )