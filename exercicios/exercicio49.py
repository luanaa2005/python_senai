# Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10

numero_list = []

for i in range(7):
    numero = int(input('Digite um numero: '))
    if numero >  10:
        numero_list.append(numero)

print(len(numero_list), 'numeros sao maiores que 10' )
    