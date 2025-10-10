#1)
# i=0
# j=0
# n=0
# while i < j:
#     i = i + 1
#     j= j - 1
#     n = n + 1
#     print(i,j,n)

#2)
# while i < 10:
#     i = i + 1
#     n = n + i + j
#     j = j + 1
#     print(i, n, j)

#////////////////////////////

#1)
# i=0
# while i < 100:
#     i = i+1
#     # O end= faz com que depois do print, ao invés de ir para a linha debaixo, faça o que estou mandando, como a ' '(um espaço, fazendo com que o while fique na mesma linha
#     2)
#     if i >= 50:
#         print(i, end=' ')
#     print(i)

#3)
# i=10
# while i > 0:
#     print(i)
#     i = i-1
# print('Fogo!')

#5)
# numero = int(input('Digite seu número: '))
# a = 0
# while a < numero:
#     a = a+1
#     if a % 2 ==0:
#         print(a)

#6)
# numero = int(input('Digite seu número: '))
# a = 0
# while a < numero:
#     a = a+1
#     if a % 2 ==1:
#         print(a)

#7)
numero = int(input('Digite seu número: '))
a = 0
soma = 0
while a < numero:
    a = a+1
    if a %2==0:
        soma = soma+a
        print(a)
print(soma)