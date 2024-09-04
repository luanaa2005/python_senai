# Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

numero1 = int(input('Digite o primeiro numero: \n'))
operacao = (input('Digite uma operacao matematica: \n'))
numero2 = int(input('Digite o segundo numero: \n'))


'''
match operacao:
    case '+' :
        print(numero1 + numero2)
    case '-': 
        print(numero1 - numero2)
    case '*' :
        print(numero1 * numero2)
    case '/': 
        print(numero1 / numero2)
'''

operacoes = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

if operacao in operacoes:
    resultado = operacoes[operacao](numero1, numero2)
    print(f'{numero1} {operacao} {numero2} = {resultado}')
else:
    print('Operacao invalida')
