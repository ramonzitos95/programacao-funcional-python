s1 = set()
s1.add('Ramon')
s1.add(1)
s1.update(('Olá Mundo', 1, 2, 3, 4))
#s1.clear()
s1.discard('Olá Mundo')
s1.discard('Ramon')
print(s1)

s2 = {1, 2, 3}
s3 = {2, 3, 4}
s4 = s2 | s3
print(s3)
s4 = s2 & s3
print(s3)
s4 = s3 - s2
print(s4)
s4 = s3 ^ s2
print(s4)
