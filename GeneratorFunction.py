def generator(n=0):
    yield 1 #pausar
    print('Continuando...')
    yield 2 #pausar
    print('Mais uma...')
    yield 3  # pausar
    print('Vou terminar...')
    return 'ACABOU'

def generator1(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return

gen = generator(n=0)
for n in gen:
    print(n)

gen = generator1(maximum=100000)
for n in gen:
    print(n)