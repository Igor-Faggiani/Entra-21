def concatenar(prefixo: str, sufixo: str):
    """ A função irá concatenar duas strings"""
    soma = prefixo + sufixo
    print(soma)

prefixo = input("Digite um prefixo: ")
sufixo = input("Digite um sufixo: ")
concatenar(prefixo, sufixo)