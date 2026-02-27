l = [] #Jeito tradicional de fazer lista
for i in range(10):
    l.append(i)
print(l)

l1 = [i for i in range(10) if i%2==0] #Jeito compactado de fazer listas, for in e if
print(l1)

l2 = [1 for i in range(10)] #Faz com que apareça o que foi escrito varias vezes
print(l2) #[1,1,1,1,1,1...]