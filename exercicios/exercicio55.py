# Desenvolva um programa que peça ao usuário para inserir um número maior que 100. Se o número for menor ou igual a 100, continue pedindo até que um número maior que 100 seja inserido

numero = int()

while numero < 100 or numero == 100 :
    numero = int(input('Digite um numero maior que 100: \n'))
