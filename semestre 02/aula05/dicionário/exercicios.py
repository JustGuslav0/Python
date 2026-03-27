def frase():
    dic = {}
    for i in 'Os ratosssss':
        if i in dic:
            dic[i]+= 1
        else:
            dic[i] = 1
    return dic

print(frase())

