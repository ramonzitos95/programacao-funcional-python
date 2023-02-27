

try:
    a = 18
    b = 0
    print(b[0])
    print('Linha 1')
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido.')
except (TypeError, IndexError) as error:
    print('Erro de tipo TypeError.')
    print('MSG', error)
    print('Nome', error.__class__.__name__)
except Exception:
    print('Erro desconhecido')

print('CONTINUAR')