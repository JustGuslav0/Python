# 1
frutas = {'banana':'amarelo',
          'uva': 'verde',
          'melancia': 'vermelha'
          }

# 2
a = frutas['uva']
print(a)

# 3
frutas['morango'] = 'vermelha'
print(frutas)

# 4
frutas['uva'] = 'roxa'
print(frutas)

# 5
rem = frutas.pop('uva')
print(rem)
print(frutas)

# 6
print('Chaves:')
for i in frutas.keys():
    print(i)

# 7
print()
print('Valores:')
for i in frutas.values():
    print(i)

# 8
check = 'banana'
if check in frutas:
    print(f'A fruta {check} está no dicionário')
else:
    print('Não encontrado!')

# 9
frutasb = { 'melancia': 'verde',
            'pessêgo': 'laranja'
            }
print(frutas)
print(frutasb)
frutas.update(frutasb)
print(frutas)

# 10
qtde = len(frutas)
print(qtde)