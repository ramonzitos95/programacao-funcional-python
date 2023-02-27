p1 = {
    'nome': 'Ramon',
    'sobrenome': 'Miranda'
}

print(p1.get('nome', 'Não existe'))

ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

p1.update({
    'nome': 'novo valor',
    'idade': 30
})

p1.update(nome='novo valor', idade=30)
tupla = ('nome', 'novo valor'), ('idade', 30)
p1.update(tupla)
print(p1)