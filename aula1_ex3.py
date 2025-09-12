#Aula 03 - variáveis
'''
import time

time.sleep(0.3)

print('Exercício 1:')
nome = input('Qual seu nome?\n')
print('Seu nome é:', nome)

time.sleep(1.5)

print('\nExercício 2:')
a = 3
b = 5
print('O resultado de 2a + 3b, considerando "a" como 3 e "b" como 5, é igual a:', 2*a + 3*b)

time.sleep(1.5)

print('\nExercício 3:')
A = int(input('\nQual o valor da variável A?:'))
B = int(input('\nAgora, qual o valor da variável B?:'))
C = int(input('\nAgora, qual o valor da variável C?:'))
print('O resultado da soma de A + B + C é igual a:', A + B + C)

time.sleep(1.5)
import time

print('\nExercício 4:')
salario = int(input('Digite seu salário:\n'))

bonus = salario * (15//100)

salarioBonus = salario + bonus

print('Parabéns! Você recebeu uma bonificação de 15% do seu salário. Seu montante este mês é:', salarioBonus)

time.sleep(1.5)

print('\nExercício 5:')
penalidade = bonus * (5/100)

salarioPenalidade = salarioBonus - penalidade

print('Porém, por 3 faltas injustificadas, você sofrerá 5% de penalidade na sua bonificação, totalizando um montante de:', salarioPenalidade)

time.sleep(1.5)

print('\nExercício 6:')

print('Método 1')
a = 10
b = 20

print('a = ', a)
print('b = ', b)

a,b = b,a

print('a =', a)
print('b =', b)

time.sleep(1.5)

print('Método 2')
print('a = ', a)
print('b = ', b)

c = a
a = b
b = c

print('\na = ', a)
print('b = ', b)

d = 1
h = 3
m = 46
s = 40

ht = d * 24 + h
mt = ht * 60 + m
st = mt * 60 + s
print(st)
segt = d * 24 * 60 * 60 + h * 60 * 60 + m * 60 + s
print(segt)


time.sleep(1.5)

print('Exercício 7:')
inputDia = int(input('Dias: '))
inputHora = int(input('Horas: '))
inputMinuto = int(input('Minutos: '))
inputSegundo = int(input('Segundos: '))

segundo = 1
minuto = 60 * segundo
hora = 60 * minuto
dia = 24 * hora

resposta = inputDia*dia + inputHora*hora + inputMinuto*minuto + inputSegundo*segundo


print('A resposta é:', resposta)

print('\nExecício 8:')

inputSegundos = input()

segundof = inputSegundos % 60
minuto = inputSegundos // 60

minutof = minuto % 60
hora = minuto // 60

horaf = hora % 24
dia = hora // 24

diaf = dia % 30
mes = dia // 30

print('minuto: ', minutof)
print('segundo: ', segundof)
print('hora: ', horaf)
print('dia: ', diaf)
print('mes: ', mes)
'''

#Aula boolean
#Exercício 1
nota = float(input('Qual sua nota: '))
aprovado = nota>=7
print('Aprovado :', aprovado)

#Exercício 2
salario = float(input('Qual seu salário: '))
imposto = salario > 1200
print('Irá pagar imposto? ', imposto)

#Exercício 3
emprestimo = salario >= 5000
print('Pode pegar empréstimo? ', emprestimo)

#Exercício 4
numero = int(input('Seu número: '))
resto = numero%2