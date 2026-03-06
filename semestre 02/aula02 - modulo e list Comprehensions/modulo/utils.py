def contarVog(x):
    soma = 0
    vogais = 'aeiou'
    for i in x:
        if i in vogais:
            soma += 1
    return soma

def revertStr(x):
    novaStr = x[::-1]
    return novaStr

def cntrPalavras(x):
    contador = 0
    if len(x) == 0:
        return 0
    for i in x:
        if i == ' ':
            contador += 1
    return contador + 1