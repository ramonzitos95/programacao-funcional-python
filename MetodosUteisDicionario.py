pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda 3',
    'idade': 900
}

pessoa.setdefault('idade', None)
print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))

print(list(pessoa.items()))