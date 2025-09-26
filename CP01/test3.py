print('oi')
velocidade = float(input('Digite sua velocidade: '))
if velocidade > 110:
    multa = (velocidade-110)*5

    mtd = """Seu limite de velocidade é excedente ao limite estabelecido.
    Métodos de pagamento:
    Pix
    Débito
    Crédito
    Digite sua escolha:
    """

    mtdPgmt = input(mtd)

    if mtdPgmt == 'Pix':
        multa = multa-multa*0.15
    if mtdPgmt == 'Crédito':
        multa = multa*1.10
    print('O total da multa é: ', multa)



print('tchau')