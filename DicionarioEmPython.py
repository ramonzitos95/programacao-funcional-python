pessoa = {
    'nome': 'Ramon Silva',
    'sobrenome': 'Santos'
}

# pessoa = dict(nome='Ramon Silva', sobrenome='Santos')

pessoa = {
    'nome': 'Ramon Silva',
    'sobrenome': 'Santos',
    'idade': 27,
    'altura': 1.8,
    'enderecos': [
        { 'rua': 'tal tal', 'numero': 123},
        { 'rua': 'outra rua', 'numero': 321},
    ]
}

print(pessoa['nome'])
print(pessoa['sobrenome'])
print()