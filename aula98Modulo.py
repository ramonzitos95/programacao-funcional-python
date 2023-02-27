#Aula para recarregar o módulo, pois o mesmo é singleton e
#uma instância em todo o programa
import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m)
    print(i)

print('Fim')