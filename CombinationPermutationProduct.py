from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodao', 'poliester']
]

# print(*list(combinations(pessoas, 2)), sep='\n')
# print(*list(permutations(pessoas, 2)), sep='\n')
print_iter(product(*camisetas))