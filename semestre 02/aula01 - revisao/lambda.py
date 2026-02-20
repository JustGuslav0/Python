# Soma das 3 funções
soma = lambda a,b,c : a + b + c

# Lambda para inverter string
inverter = lambda a : a[::-1]
print(inverter('oii'))

verifica = lambda a: a == a[::-1]

verifica2 = lambda a: a if a == a[::-1] else 'Não é!'

