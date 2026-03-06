#Metodo de import 1
from modulos import * #Faz com que seja importado tudo que tenha no arquivo
a = dobro(2)
b = triplo(2)
print(a,b)

#Metodo de import 2
import modulos #Mais dificil, porem melhor quando voce quer saber exatamente de onde saiu e quando não quiser sobrepor alguma função por ter uma possível duplicidade
a = modulos.dobro(10) #Tem que sempre falar o lugar que ta importando quando for chamar
b = modulos.triplo(10)
print(a,b)

#Metodo de import 2 porem de outra forma
import modulos as m
a = m.dobro(10) #Faz com que consiga colocar nomes nos imports
b = m.triplo(10)
print(a,b)

#Vai fazer com que mostre diversos modulos
help()
