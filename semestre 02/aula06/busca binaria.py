l = [12, 25, 37, 39, 41, 53, 59, 68, 71, 95]

def busca_binaria(l, chave):
    inicio = 0
    final = len(l) - 1
    while inicio <= final:
        meio = (inicio + final)//2
        if chave < l[meio]:
            final = meio - 1
        elif chave > l[meio]:
            inicio = meio + 1
        else:
            return meio
    return -1