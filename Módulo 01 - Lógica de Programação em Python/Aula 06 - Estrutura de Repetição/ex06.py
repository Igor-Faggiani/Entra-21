for i in range(1, 101):

    txt = ''

    if i % 3 == 0:
        txt += 'fizz'

    if i % 5 == 0:
        txt += 'buzz'

    if txt == '':
        txt = i

    print(txt)