# CRUD = Create Read Update Delete

# cavaleiros = ['Seya','Aldebaran', 'Aldebaran', 'Shun', 'Shiryu', 'Yoga']
# print(cavaleiros)

# # adicionando um novo elemento ao final da lista
# cavaleiros.append('Ikki')
# print(cavaleiros)

# # extendendo a lista com outra lista
# cavaleiros.extend(['Shina', 'Maryn'])
# print(cavaleiros)

# # inserindo na lista em uma posição específica
# cavaleiros.insert(0, 'Athena')
# print(cavaleiros)

# # remove, exclui um elemento pelo valor
# cavaleiros.remove('Shun')
# print(cavaleiros)

# # pop - exclui o ultimo elemento da lista ou o indice informado
# elemento = cavaleiros.pop()
# print(elemento)
# cavaleiros.pop(0)
# print(cavaleiros)

# # index - retorna o indice da primeira ocorrência de um valor procurado
# print(cavaleiros.index('Yoga'))

# # concatenação de métodos
# cavaleiros.pop(cavaleiros.index('Yoga'))
# print(cavaleiros)

# # alterando valor de um elemento da lista
# cavaleiros[cavaleiros.index('Ikki')] = 'Ikki de fenix'
# print(cavaleiros)

# # contabilizando elementos repetidos 
# print(cavaleiros.count('Aldebaran'))


# sort - ordenar a lista de forma crescente 
frutas = ['morango', 'maça', 'abacaxi', 'kiwi', 'amora', 'umbu', 'laranja', 'bergamota']
numeros = [9, 5, 81, 100, 33, 21, 2]

frutas.sort()
numeros.sort()

print(frutas)
print(numeros)

# reverse - ordenar a lista de forma decrescente
frutas.reverse()
numeros.reverse()

print(frutas)
print(numeros)

# deletar um elemento da lista
del frutas[0]
print(frutas)

# limpar a lista
frutas.clear()
print(frutas)