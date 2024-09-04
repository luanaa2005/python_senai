# Cadatrso de alunos
from os import system
import operacoes as op
# from operacoes import menu, listar_nomes
# import operacoes

operacao = 'sim'
matricula = 0

while operacao == 'sim':
    op.menu()
    opcao = int(input('Informe a ação desejada: '))

    match opcao:
        case 1:
            nome = input('Qual nome deseja cadastrar: ')
            email = input('Informe o mail do aluno:')
            data_nascimento = input('Informe a data de nascimento:')

            matricula += 1
            op.cadastrar_nome(nome, email, data_nascimento, matricula)
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
    