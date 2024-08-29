#  Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido


maior = None
for pergunta in range(5):
    numero = int(input('Digite um numero: '))
    if maior is None or  numero > maior:
        maior = numero

print('maior numero: ' , maior)
