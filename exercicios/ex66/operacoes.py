nomes = []

def menu():
    opcoes = ['Cadastrar nome', 'Atualizar o nome', 'Excluir', 'Listar todos os cadastrados']
    for indice, opcao in enumerate(opcoes):
        print(f'{indice + 1} - {opcao}')

def listar_nomes():
     for indice, nome in enumerate(nomes):
             print(f'{indice} - {nome}')

def cadastrar_nome(nome):
    nomes.append(nome)

def atualiza_nome(nome, novo_nome):
    nomes[nomes.index(nome)] = novo_nome      # index retorna em qual indice o nome está na lista

def excluir_nome(nome):
    nomes.remove(nome)