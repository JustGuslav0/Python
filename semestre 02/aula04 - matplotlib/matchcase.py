dia = 3
#Utilizando match
match dia:
    case 1:
        print('Sexta')
    case 2:
        print('Sábado')
    case 3:
        print('Domingo')
    case _:
        print('Outro dia')

#Utilizando if
if dia == 1:
    print('Sexta')
elif dia == 2:
    print('Sábado')
elif dia == 3:
    print('Domingo')
else:
    print('Outro dia')


