# Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos

soma = 0

for pergunta in range(10):
    numero = int(input('Digite um numero: '))
    soma += numero
    
print(f'media dos numeros inseridos: {soma / 10} '  ) 
