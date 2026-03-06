import mat1
import mat2
op = input('Digite o que deseja(+,-,*,/): ')
x = float(input('Digite o primeiro valor: '))
y = float(input('Digite o segundo valor: '))

res = 0
if op in '+-*/':
    if op == '+':
        res = mat1.soma(x,y)
    elif op == '-':
        res = mat1.subtracao(x,y)
    elif op == '*':
        res = mat2.multiplicacao(x,y)
    elif op == '/':
        res = mat2.divisao(x,y)
    print(f'O resultado de {x}{op}{y} = {res}')
else:
    print('Operação inválida')

