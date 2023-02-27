x = 1

def escopo():
    global x
    x = 10
    def outra_funcao():
        y = 2
        print(x)
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)