# Crie um programa que peça ao usuário para inserir números até que ele digite o número 0. Ao final, exiba a soma de todos os números inseridos (exceto o 0)

numero = int(input('informe o numero \n'))
soma = 0

while numero != 0:
    soma = numero + soma
    numero = int(input('informe o numero \n'))
print(soma)

   
    
    