# Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista


numeros_list = []
soma = 0
for i in range(5):
    numero = int(input('Digite um numero: '))
    numeros_list.append(numero)
    soma = numero + soma
   
print('\nlista de numeros: ', numeros_list)
print('soma dos numeros: ', soma), '\n'

        
'''
numero1 = int(input('Insira um numero: \n'))
numero2 = int(input('Insira um numero: \n'))
numero3 = int(input('Insira um numero: \n'))
numero4 = int(input('Insira um numero: \n'))
numero5 = int(input('Insira um numero: \n'))


numeros = [numero1, numero2, numero3, numero4, numero5]
print()
print('lista de numeros: ')
for i in numeros:
    print(i)
print()
print('Soma de todos os numeros da lista: \n', numero1 + numero2 + numero3 + numero4 + numero5)
'''

# pesquisei outro metodo de soma:

# print('Soma de todos os numeros da lista: \n')
# soma = sum(numeros)
# print(soma)





    



    


