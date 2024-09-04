# Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente


mes = int(input('Digite um mes: \n'))

if mes > 2 and mes < 7:
    print('outono')
elif mes > 6 and mes < 10:
    print('inverno')
elif mes > 8 and mes < 13:
    print('primavera')
else:
    print('verao')

