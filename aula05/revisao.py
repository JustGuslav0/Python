#pi = (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13-1/15+1/17)*4
'''def pi(c):
    soma = 0
    for i in range(c):
        soma += 1/(2*i+1)*(-1)**i
    return 4*soma

a = pi(10)
#'''
#print(a)
'''
a = ['Joao', 'Maria', 'Beatriz']
print(a)
a.append('Helder')
print(a)
a.pop(1)
print(a)
range(10) -> [0,1,2,3,4,5,6,7,8,9]
range(3, 10) -> [3,4,5,6,7,8,9]
range(4,10,2) -> [4,6,8]
for i in range(10):
    print(i)'''



def hipotenusa(c1,c2):
    return (c1**2 + c2**2)**(1/2)

print(hipotenusa(3,4))