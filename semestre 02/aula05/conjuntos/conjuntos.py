lista = [1,9,4]
lista2 = [1,3,4,5,6]
conjunto = set(lista)
conjunto2 = set(lista2)

#1
igual = conjunto & conjunto2
print(igual)

#2
res = conjunto-conjunto2
print(list(res))

#3
res2 = conjunto2-conjunto
print(list(res2))

#4
res3 = (conjunto|conjunto2) - (conjunto&conjunto2)
lis3 = list(res3)
print(conjunto,conjunto2)
print(lis3)