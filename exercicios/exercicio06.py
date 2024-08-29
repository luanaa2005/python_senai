# Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

numero1 = float(input('digite o primeiro numero: \n'))
numero2 = float(input('digite o segundo numero: \n'))
operacao = str(input('Digite uma operacao matematica: \n'))



match operacao:
    case '+' :
        print(numero1 + numero2)
    case '-': 
        print(numero1 - numero2)
    case '*' :
        print(numero1 * numero2)
    case '/': 
        print(numero1 / numero2)

    
    
    
