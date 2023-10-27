lista_string = ["Olá, meu nome é Igor."]

qnt_palavras = tuple(len(string.split()) for string in lista_string)

print(qnt_palavras)