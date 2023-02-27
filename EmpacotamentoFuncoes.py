
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args):
    print(args, type(args))
    total = 0
    for numero in args:
        total = total + numero
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

soma_7_8_9 = soma(7, 8, 9)
print(soma_7_8_9)

print(soma(1, 2, 3, 4, 5, 6, 7, 8, 9))

numeros = 1, 2, 3, 5, 6, 7, 8, 90, 20
outra_soma = soma(*numeros)
print(outra_soma)

print(numeros)