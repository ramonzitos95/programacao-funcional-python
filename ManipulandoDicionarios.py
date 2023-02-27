pessoa = {}

pessoa['nome'] = 'Ramon Silva'
pessoa['sobrenome'] = 'Santos'
chave = 'nome'


print(pessoa[chave])


pessoa[chave] = 'Silvas'

del pessoa['sobrenome']
print(pessoa)