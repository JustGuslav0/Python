# #Banco com deposito, saque e extrato
# saldo = 0
# transacoes = []
#
# def depositar(valor):
#     global saldo
#     saldo += valor
#     transacoes.append(valor)
#     return saldo
#
# def sacar(valor):
#     global saldo
#     saldo -= valor
#     transacoes.append(-valor)
#     return saldo
#
# def extrato():
#     for i in transacoes:
#         print(f'R${i:.2f}')
#     print(f'R${saldo:.2f}')
#
# while True:
#     op = input('Digite o que deseja (1) sacar; (2) depositar; (3) extrato; outro para sair!')
#     if op == '1':
#         valor = float(input('Digite o valor para o saque:'))
#         sacar(valor)
#     elif op == '2':
#         valor = float(input('Digite o valor para o saque:'))
#         depositar(valor)
#     elif op == '3':
#         extrato()
#     else:
#         break

# Carrinho de compras
c = []

def adicionar_produto(produto):
    c.append(produto)

def remover_produto(produto):
    for i in range(len(c)): #
        if produto == c[i]:
            c.pop(i)
            break

def ver_carrinho():
    for i in c:
        print(i)

while True:
    op = input('(1) add; (2) remove; (3) checkout;(else) exit')
    if op == '1':
        produto = input('Digite o nome do produto:')
        adicionar_produto(produto)
        print()
    elif op == '2':
        produto = input('Digite o nome do produto:')
        remover_produto(produto)
        print()
    elif op == '3':
        ver_carrinho()
        print()
    else:
        break