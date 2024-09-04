nomes = []
matricula = 1

def menu():
    opcoes = ['Cadastrar aluno', 'Atualizar aluno', 'Excluir cadastro', 'Listar todos os cadastrados']
    for indice, opcao in enumerate(opcoes):
        print(f'{indice + 1} - {opcao}')

def listar_nomes():
     for indice, nome in enumerate(nomes):
             print(f'{indice} - {nome}')

def cadastrar_nome(nome, email, data_nascimento, matricula):

    aluno = {
     'nome': nome, 
     'email': email, 
     'data_nscimento': data_nascimento,
     'matricula': matricula
    }

    nomes.append(aluno)

def atualiza_nome(nome, novo_nome):
    nomes[nomes.index(nome)] = novo_nome      # index retorna em qual indice o nome está na lista

def excluir_nome(nome):
    nomes.remove(nome)