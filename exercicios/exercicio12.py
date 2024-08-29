# Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente

transporte = str(input('Escolha um meio de trasnporte (carro, bicicleta, a pé): \n'))



match transporte:
    case 'carro' :
        print('velocidade média: 100 km/h', )
    case 'bicicleta': 
        print('velocidade media: 25 km/h')
    case 'a pe' :
        print('velocidade media: 3,6 km/h')
    