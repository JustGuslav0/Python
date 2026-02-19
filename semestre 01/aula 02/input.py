# input('Escreva seu nome: ').stripper() deixa sem espaço a resposta do user
# input('Escreva seu nome: ').upper() deixa tudo em caps lock a resposta do user


diaUser = int(input('Quantos dias com o carro alugado: '))
kmUser = float(input('Quantos km rodados com o carro alugado: '))

calculo = diaUser*60 + kmUser*0.15

print('O total que você deve pagar é: R$', calculo)