y = int(input('Quantidade de linhas da matriz: '))
x = int(input('Quantidade de colunas: '))
matriz = []
for i in range(y):
    lista = []
    for j in range(x):
        lista.append(input(f'Digite o elemento: '))
    matriz.append(lista)

print(matriz)