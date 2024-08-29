# Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5

numero1 = float(input('Digite um numero: \n'))
numero2 = float(input('Digite outro nummero: \n'))

if numero1 % 5 == 0 and numero2 % 5 == 0:
    print('ambos sao multiplos de 5')
else:
    print('nao sao multiplos de 5')