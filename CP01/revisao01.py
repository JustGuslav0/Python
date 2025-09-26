numero = int(input('Digite seu número: '))

par = (numero%2) == 0

impar = (numero%2) == 1

if numero < 100:
    if par:
        print('Seu número é par e menor que 100')
    if impar:
        print('Seu número é ímpar e menor que 100')
if numero > 100:
    if par:
        print('Seu número é par e maior que 100')
    if impar:
        print('Seu número é ímpar e maior que 100')
if numero == 100:
    if par:
        print('Seu número é par e igual que 100')
    if impar:
        print('Seu número é ímpar e igual que 100')