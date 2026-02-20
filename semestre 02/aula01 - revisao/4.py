def pi(qtde):
    soma = 0
    for i in range(qtde):
        #
        x = (-1)**i * (2*i+1) 
        soma = soma + 1/x
    return 4*soma

pi(4)