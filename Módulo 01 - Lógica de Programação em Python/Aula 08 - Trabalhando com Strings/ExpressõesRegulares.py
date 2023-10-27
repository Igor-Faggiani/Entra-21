"""
Expressões regulares - São uma sequência de caracteres que definem um padrão
em uma string.
"""
import re

texto = """Python é uma linguagem de programação poderosa.\n
JavaScript e Python são linguagens similares.
"""

# Busca de padrões
padrao = r"\bp\w+"

palavras_encontradas = re.findall(padrao, texto, flags=re.I | re.S)
print(palavras_encontradas)

# Validação de dados
email = "usuario@email.com"

padrao = r"^\w+@\w+\.\w+$"
if re.match(padrao, email):
    print("E-mail válido")
else:
    print("E-mail inválido")

# Substituição de padrões
texto = "Eu amo programação com JavaScript!"

padrao = r"javascript"
texto = re.sub(padrao, "Python", texto, flags=re.I)
print(texto)

# Extraindo informação
telefones = """(47) 9 9999-9999
47 99999-9999
"""
padrao = r"\((\d+)\) 9 \d{4}-(\d{4})"

telefone_encontrado = re.search(padrao, telefones)
if telefone_encontrado:
    print(f"Telefone: {telefone_encontrado.group(0)}")
    print(f"DDD: {telefone_encontrado.group(1)}")
    print(f"Últimos 4 dígitos: {telefone_encontrado.group(2)}")


ruas = """R. Alberto Stein, 416 - Velha, Blumenau - SC, 89036-200"""

padrao = r"^([\w\s\.]+),\s(\d+)\s-\s(\w+),\s(\w+)\s-\s(\w{2}),\s(\d{5}-\d{3})$"

endereco_encontrado = re.search(padrao, ruas)
if endereco_encontrado:
    print(f"""
Endereço: {endereco_encontrado.group(0)}
Rua: {endereco_encontrado.group(1)}
Número: {endereco_encontrado.group(2)}
Bairro: {endereco_encontrado.group(3)}
Cidade: {endereco_encontrado.group(4)}
Estado: {endereco_encontrado.group(5)}
CEP: {endereco_encontrado.group(6)}
""")

