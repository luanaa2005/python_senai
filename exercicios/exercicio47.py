# Crie um programa que peça ao usuário um número e exiba a tabuada desse número de 1 a 10

num = int(input('Digite um numero: '))

for numero in range(10):
    print(num, 'x' , numero + 1 , ':' , (numero + 1) * num)
