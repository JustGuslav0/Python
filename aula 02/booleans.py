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
par = numero%2 == 0
print('É par: ', par)

#Exercício 5
numero = int(input('Seu número: '))
numero2 = int(input('Seu número: '))
impariedade = numero%2 != numero2%2
print('Impariedade?', impariedade)
