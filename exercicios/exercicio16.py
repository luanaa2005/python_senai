# Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro

combustivel = str(input('Escolha um tipo de combustivel (gasolina, etanol, diesel): \n'))



match combustivel:
    case 'gasolina' :
        print('preço por litro: R$ 6,13', )
    case 'etanol': 
        print('preço por litro: R$ 3,01')
    case 'diesel' :
        print('preço por litro: R$ 6,03')