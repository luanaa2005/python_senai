# Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente

estado = str(
    input('Informe o seu estado civil (solteiro, casado, divorciado, viúvo): \n'))

match estado:
    case 'solteiro':
        print('estado civil: ', estado)
    case 'casado':
        print('estado civil: ', estado)
    case 'divorciado':
        print('estado civil: ', estado)
    case 'viuvo':
        print('estado civil: ', estado)
