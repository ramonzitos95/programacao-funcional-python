#Generator expression, Iterables e Iterators em python

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()  #tem __iter__e__next__

lista = [n for n in range(10000)]
generator = (n for n in range(10000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)