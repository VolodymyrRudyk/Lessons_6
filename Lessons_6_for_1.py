D = {'a' : 1, 'b' : 2, 'c' : 3}
print(D)

Ks = list(D.keys())                     #невпрорядкований список ключів словника D
print(Ks)

Ks.sort()                               #сортований список ключів
print(Ks)

for key in Ks:                          #дослівно: для key в Ks
    print(key, '=>', D[key])            #вивід на екран

for key in sorted(D):                   #ще один метод сортування
    print(key, '=>', D[key])