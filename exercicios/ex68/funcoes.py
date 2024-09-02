

def menu():
    opcoes = ['Cadastrar aluno', 'Atualizar cadastro', 'Excluir cadastro', 'Listar cadastros', 'Buscar cadastro']
    for indice, opcao in enumerate(opcoes):
        print(f'{indice + 1} - {opcao}')


def cadastro():
    nome = input('Digite o nome: ')
    email = input('Digite o email: ')
    data = input('Informe a data de nascimento: ')


def gerador_matricula():
    matricula = 12344
    matricula = matricula + 1
    print('Numero da matricula: ', matricula)


