# Escreva um
# algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 2- atualizar o
# nome, 3, excluir, 4-listar todos os cadastrados, ao final da operação deve dar
# uma mensagem indicando o resultado da operação e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for
# inserida.

nomes = ['Luciano', 'Lucas', 'Matheus']
operacao = 'sim'

while operacao == 'sim':
    print('1- Cadastrar nome')
    print('2- Atualizar o nome')
    print('3- Excluir')
    print('4- Listar todos os cadastrados')
    opcao = int(input('Informe a ação desejada: '))

    match opcao:
        case 1:
         nome = input('Digite o nome: ')
         nomes.append(nome)
        case 2:
         nome = input('Qual nome será atualizado? ')
         novo_nome = input('Digite o novo nome: ')

         nomes[nomes.index(nome)] = novo_nome      # index retorna em qual indice o nome está na lista
        case 3:
         nome = input('Qual nome será removido? ')
         nomes.remove(nome)
        case 4:
         for indice, nome in enumerate (nomes):
             print(f'{indice} - {nome}')
        case _:
         print('opcao invalida')

    operacao = input('Deseja realizar outra operacao? ').lower()

    if operacao == 'nao':
        break

       


