l = [10,20,30,40,3.45,1.0]
print(len(l))
k = 0
soma = 0
#O len() faz com que leia a quantidade de valores dentro da lista, começando no 1 mesmo
while k < len(l):
    soma += l[k]
    k+=1
print(soma, soma/len(l))

#Cria uma lista vazia
animais = []
print(animais)
#O .append serve para adicionar um valor na lista
animais.append('Gato')
print(animais)

#Já o .pop(), faz com que seja removido algum valor de determinada posição ou a lista inteira, depende do que coloca dentro do ()
    #.pop() não consegue retirar algum valor escrito, como 'Gato', apenas a posição
        #.pop() tira o valor de uma posição e o próximo se torna ele, normal
gato = animais.pop()
print(gato)

#.extend() faz com que seja somado uma lista dentro da lista original, porém a soma de lista é uma concatenação de lista, se torna uma só
animais.extend([1,2])
#Mesma coisa que o comando abaixo, que faz uma lista só, porém com os valores juntos
a = animais + [1,2]

#for é um laço de repetição que é mais pratico que o while
#O for variavel in tem que ser em uma lista, ou o range, caso não seja em lista dará erro
for i in animais:
    print(i)

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = a
d = b

soma = 0

#1)
for i in range(a,b+1,1):
    print(i)
    soma += i

print(soma)
print(soma/len(range(a,b+1)))

#2)
while c <= d:
    print(c)
    c+=1
