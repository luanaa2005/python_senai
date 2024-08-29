# Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente



mes = int(input('Digite um mes: \n'))

if mes >= 3 and mes <= 6:
    print('outono')
elif mes >= 7 and mes <= 9:
    print('inverno')
elif mes >= 10 and mes <= 11:
    print('primavera')
else:
    print('verao')
    

    