import matplotlib.pyplot as plt
#1
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

#2
# x = [i for i in range(-100, 101)]
# y = [i**2 for i in x]

#3
# x = [i for i in range(0, 101)]
# y = [i**0.5 for i in x]

#4
# x = [i for i in range(-100, 101)]
# y = [3*i**2 - 10*i+8 for i in x]

plt.plot(x,y, marker='o', linestyle='-')
plt.title('Gráfico de Coordenadas x, y')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.grid(True)
plt.show()