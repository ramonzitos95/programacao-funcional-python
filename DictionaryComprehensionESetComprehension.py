produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

for chave, valor in produto.items():
    print(chave, valor)

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}

lista = {
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
}

print(dict(lista))

print(dc)

s1 = {i ** 2 for i in range(10)}
print(s1)