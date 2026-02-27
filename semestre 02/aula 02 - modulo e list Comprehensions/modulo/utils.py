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