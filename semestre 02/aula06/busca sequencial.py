lista = [1,2,3,4,5,6,7,8,9,10]

def procurar(lista, chave):
    for i in range(len(lista)-1):
        if chave == lista[i]:
            return i
    return -1
print(procurar(lista,3))