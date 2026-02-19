numero = 5
enquanto = 5

multiplicacao = 5

while enquanto > 0:
    if enquanto == 1:
        break
    multiplicacao = multiplicacao*(enquanto-1)
    enquanto-=1

print(multiplicacao)
print(5*4*3*2*1)

# num = int(input('Digite um numero:'))
#
# fat = 1
# i = 1
#
# while i <= num:
#     fat = fat * i
#     i = i + 1
#
# print("seu numero é:", fat)