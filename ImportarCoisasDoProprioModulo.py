import aula97_m
from aula97_m import soma, variavel_modulo

print('Este módulo se chama', __name__)
variavel_modulo = 'Luiz'
print(aula97_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula97_m.soma(2, 3))


def soma(x, y):
    return x + y