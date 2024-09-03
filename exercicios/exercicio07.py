# Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if

nota = int(input('Digite uma nota de o a 10: \n'))

if nota > 7:
    print('nota alta')
elif nota == 7:
    print('nota media')
else:
    print('nota baixa')
