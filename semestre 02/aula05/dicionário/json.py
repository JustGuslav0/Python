#Um dicionário (JSon) em python
pessoa = {
    'nome': 'Helder',
    'idade': 35,
    3.14: ['sorvete','uva']
}
print(pessoa)
rem = pessoa.pop('nome')
print(pessoa, rem)
#pessoa['altura'] = 1.73
#print(pessoa)
#a = list(pessoa.keys())
#print(a)
#for j in pessoa.keys():
#    print(j)

#for i in pessoa.values():
#    print(i)
#for (k,j) in pessoa.items():
#    print(f'chave:{k}; valor:{j}')


dic_a = {"A": "Avião", "B": "Barco"}
dic_b = {"B": "Balão", "C": "Carro"}
print(dic_a)
print(dic_b)
dic_a.update(dic_b)
print(dic_a)
print(dic_b)

dic_a = ["A", "B"]
dic_b = ["A", "B"]
a = dict(zip(dic_a,dic_b))
print(a)


#Para separar string