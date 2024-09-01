# Sistema de cadastro de alunos

from os import system
import funcoes as fun
operacao = 'sim'

while operacao == 'sim':
    fun.menu()
    opcao = int(input('Informe a ação desejada: '))

    match opcao:
        case 1:
            fun.cadastro()
            fun.gerador_matricula()
    #     case 2:
    #         nome = input('Qual nome será atualizado? ')
    #         novo_nome = input('Digite o novo nome: ')
    #         op.atualiza_nome(nome, novo_nome)
    #     case 3:
    #         nome = input('Qual nome será removido? ')
    #         op.excluir_nome(nome)
    #     case 4:
    #         op.listar_nomes()
    #     case _:
    #      print('opcao invalida')

    # operacao = input('Deseja realizar outra operacao? ').lower()
    # system('clear')

    # if operacao == 'nao':
    #     break
    