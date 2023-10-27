turno = input('Diga o turno do dia em que você estuda, (M) matutino, (V) vespertino e (N) noturno: ')

match turno:
    case 'm':
        print('Bom dia!')
    case 'v':
        print('Boa tarde!')
    case 'n':
        print('Boa noite!')
    case 'M':
        print('Bom dia!')
    case 'V':
        print('Boa tarde!')
    case 'N':
        print('Boa noite!')
    case _:
        print('Valor inválido!')
