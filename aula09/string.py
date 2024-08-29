
texto = 'luana Carvalho de Almeida    '
texto2 = texto.capitalize()

# capitalize muda o primeiro caracter da string para maiusculo

print(texto.capitalize())
print(texto2)

# lower padroniza a string em minusculo

nome = 'LuAnA cArvAlHo dE aLmeidA'
nome2 = 'luana carvalho de almeida'

if nome.lower() == nome2.lower():
    print('sao iguais')
else:
    print('nao sao iguais')


# upper transforma uma string em maiusculo

print(nome.upper())

# replace muda um padrao de caracteres de uma string

silvano_sales = 'coração coração cabeção'
# silvano_sales2 = silvano_sales.replace('ç', 'c')
# silvano_sales2 = silvano_sales2.replace('ã','a')
print(silvano_sales.replace('çã', 'ca'))

# strip remove caracteres em branco no final e no inicio de uma string

jack_stripador = '               removendo espaços de uma string                '

print(jack_stripador)
print(jack_stripador.strip())

# split divide uma string em elementos de uma lista

string_espalhada = 'Luana Carvalho de Almeida'
print(string_espalhada.split())

# join transforma os elementos de uma lista em uma string
# concatena strings 

nome_lista = ['Luana', 'Carvalho', 'de', 'Almeida']

print(' '.join(nome_lista))

# slice manipula string por indice 

cidade = 'recanto das emas, cidade do povo'
print(cidade[12:16])
print(cidade[::-1])


palindromo = 'arara'
if palindromo.lower() == palindromo[::-1].lower():
    print('é palindromo')
else:
    print('nao é palindromo')


