numero = int(input('Digite seu número: '))

par = (numero%2) == 0

impar = (numero%2) == 1

if numero < 100 and par:
    print('Seu número é par e menor que 100')
if numero < 100 and impar:
    print('Seu número é impar e menor que 100')
if numero == 100 and par:
    print('Seu número é par e igual a 100')
if numero == 100 and impar:
    print('Seu número é impar e igual a 100')
if numero > 100 and par:
    print('Seu número é par e maior que 100')
if numero > 100 and impar:
    print('Seu número é impar e maior que 100')