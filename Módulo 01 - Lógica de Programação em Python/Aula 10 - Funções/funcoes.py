# Sintaxe de uma função
def nome_funcao(parametro1, parametro2):
    ...


# Parâmetros
def lava_louca(nome):
    print(f"{nome} está lavando a louça 🍽")


# Parâmetro padrão
def limpa_chao(nome="Alexandre"):
    print(f"{nome} está limpando o chão 🧹")


def faz_comida():
    print("Alison está fazendo a comida 🥗")


# Docstring
def soma(a: int, b: int) -> int:
    """Retorna a soma entre a e b"""
    return a + b


# Escopo das funções
PI = 3.1415


def dividir_por_pi(numero):
    resultado = numero / PI
    return resultado


# Funções recursivas
def fatorial(n):
    if n == 0:
        return 1

    return n * fatorial(n - 1)


# Funções variádicas
def somar_numeros(*args: int) -> int:
    return sum(args)


# Kwargs
def funcao_com_kwargs(**kwargs) -> None:
    for chave, valor in kwargs.items():
        print(f"Chave: {chave} | Valor: {valor}")


if __name__ == "__main__":
    lava_louca("Alexandre")
    limpa_chao("William")
    faz_comida()
    print(soma(10, 20))
    print(dividir_por_pi(10))
    print(fatorial(10))
    print(somar_numeros(1, 2, 3, 4, 5))
    funcao_com_kwargs(nome="William", idade=23, email="contato.williamc@gmail.com")