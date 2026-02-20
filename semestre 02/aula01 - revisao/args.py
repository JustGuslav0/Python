#1
def soma(*args):
    calculo = 0
    for i in args:
        calculo += i
    return calculo

print(soma(1,3,66))

#Pegando notas em uma lista usando *
l = []
qtnd = int(input('Digite a qntd de notas: '))
for i in range(qtnd):
    l.append(float(input(f'Digite a nota {i+1}: ')))
print(l)

#Media utilizando *args
def media(*args):
    calculo = 0
    for i in args:
        calculo += i
    return calculo/len(args)

print(media(*l))

#Colocar as strings que quiser em uma unica string
def printa(*args):
    texto = ''
    for i in args:
        texto += i + ' '
    return texto[:-1]

print(printa('aoba', 'penis'))

