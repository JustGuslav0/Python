# # Utilizar % (junto do tipo da variavel)  dentro da string e fora (junto da variavel) faz com que a variavel entre na string:
# x = 10
# a = 'Eu me chamo Gustavo tenho %d anos' %x
# print(a)
#
# #Consigo utilizar % e dar valor a varias variaveis:
# x = 10
# y = 20
# z = 15
# a = 'Numeros que gosto: %d %f %d' %(x,y,z)
# print(a)
#
# #tipos para %:
# #d = int
# #f = float
# #s = string
#
# #Além desse, consigo utilizar {} com .format
# x = 10
# y = 20
# z = 15
#     #{:} faz com que voce consiga colocar o tipo da variavel
#     #{:^s} faz com que a string fique no meio, {:<s} faz com que a string fica a esquerda, {:>s} faz com que a string fica a direita
#     #Além disso, {:.<10s} faz com que fiquem completados os espaços com pontos na direita do texto
# a = ('Numeros que gosto: {:.<10d} {:.2f} {:.3f}') .format(x,y,z)
# print(a)

#Outro jeito (o melhor) é com o (f'')
print('-'*20)
print(f'|{"id":2s} | {"Vinhos":<10s} | {"Valor":9s}|')
print(f"""|{"1":2s} | {"Vinho Ag":<10s} | R${100:7.2f}|""")
print(f"""|{"1":2s} | {"Vinho Ber":<10s} | R${85:7.2f}|""")
print(f"""|{"1":2s} | {"Vinho Vic":<10s} | R${70:7.2f}|""")
print('-'*20)