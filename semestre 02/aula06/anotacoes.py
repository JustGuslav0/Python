# selection sort
l = [6, 5, 4, 3, 2, 1]
print(l)
def index_menor(l, inicio):
    menor = l[inicio]
    im = inicio
    for i in range(inicio, len(l)):
        if menor > l[i]:
            menor = l[i]
            im = i
    return im

for i in range(len(l)):
    a = index_menor(l,i)
    aux = l[i]
    l[i] = l[a]
    l[a] = aux

print(l)


#insertion sort
l = [9, 8, 7, 6, 5]
print(l)
for i in range(1,len(l)):
    #i = len(l) - 1
    aux = l[i]
    j = i - 1
    while aux < l[j] and j>=0:
        l[j+1] = l[j]
        j = j -1
    l[j+1] = aux
    print(l)


l = [3, 5, 7, 9, 6]
def busca_sequencial(l, chave):
    for i in range(len(l)):
        if chave == l[i]:
            return i
    return -1