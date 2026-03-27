from os import error

import requests


#
# r = requests.get(url)
# a = r.text
# print(a)
# print(type(a))
def consultaCep():
    cep = input('Digite seu CEP: ')
    url = 'https://viacep.com.br/ws/'
    inputCep = url + cep + '/json/'
    r = requests.get(inputCep)
    dic = r.json()
    x,y,z = dic['cep'],dic['logradouro'],dic['bairro']
    lista = x, y, z
    return lista
print(consultaCep())