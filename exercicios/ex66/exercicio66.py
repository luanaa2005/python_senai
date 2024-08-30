# Escreva um
# algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o
# nome, 3, excluir, 4-listar todos os cadastrados, ao final da operação deve dar
# uma mensagem indicando o resultado da operação e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for
# inserida.

from os import system
import operacoes as op
# from operacoes import menu, listar_nomes
# import operacoes

operacao = 'sim'

while operacao == 'sim':
    op.menu()
    opcao = int(input('Informe a ação desejada: '))

    match opcao:
        case 1:
            nome = input('Digite o nome: ')
            op.cadastrar_nome(nome)
        case 2:
            nome = input('Qual nome será atualizado? ')
            novo_nome = input('Digite o novo nome: ')
            op.atualiza_nome(nome, novo_nome)
        case 3:
            nome = input('Qual nome será removido? ')
            op.excluir_nome(nome)
        case 4:
            op.listar_nomes()
        case _:
         print('opcao invalida')

    operacao = input('Deseja realizar outra operacao? ').lower()
    system('clear')

    if operacao == 'nao':
        break
    