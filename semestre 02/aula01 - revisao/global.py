def f1(a):
    print(a+x)

def f3(a):
    global x
    x = x+1
    print(a+x)

x=4
f1(3)
print(f3(3))
print(x)

#1
saldo = 0
transacoes = []

def depositar(valor):
    global saldo
    saldo += valor
    return saldo

def sacar(valor):
    global saldo
    saldo -= valor
    return saldo

def extrato():
    global transacoes
