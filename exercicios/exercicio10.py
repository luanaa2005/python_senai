# Crie um algoritmo que solicite ao usuário uma idade e verifique se ela é maior ou igual a 18

idade = int(input('Digite sua idade: \n'))

if idade > 18:
    print('idade maior de 18')
elif idade == 18:
    print('idade igual a 18')
else:
    print('idade menor de 18')
