# Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1

numero = int(input('Informe um numero: \n'))
from os import system
import time

for i in range(numero):
    system('clear')
    print(numero - i)
    time.sleep(1)


