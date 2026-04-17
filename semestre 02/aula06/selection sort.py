def selectionSort(lista,ind):
    iMenor = 0
    menor = lista[ind]
    for i in range(len(lista)):
        if menor > lista[i]:
            menor = lista[i]
            iMenor = i
    return iMenor

# lista = []
# while True:
#     x = int(input('Digite o valor que gostaria de acrescentar na lista, 0-sair '))
#     if x == 0:
#         index = int(input("Digite o começo que gostaria: "))
#         print(lista)
#         break
#     if x != 0:
#         lista.append(x)

print(selectionSort([12,5,6,7],0))