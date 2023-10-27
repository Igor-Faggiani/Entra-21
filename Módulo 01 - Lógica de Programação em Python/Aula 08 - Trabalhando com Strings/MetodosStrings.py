"""
Strings - São sequências de caracteres
"""

# Tamanho de uma string
print(len("William"))

# Transformar a string (maiúsculas, minúsculas e capitalização)
# nome = input("Digite o seu nome: ").title()
# print(nome)

# Remover espaços
email = "    william@email.com       "
email = email.strip()
print(email)

# Transformar a string em vetor
texto = "Ana, Maria, Pedro, João, Joaquim"
nomes = texto.split(", ")
print(nomes)

# Substituir palavras na string
texto = "Ana, Maria, Pedro, João, Joaquim, Ana"
texto = texto.replace("Ana", "Beatriz")
print(texto)

# Encontrar um padrão de string
texto = "Ana, Maria, Pedro, João, Joaquim"
indice = texto.find("Mara")

indice = texto.index("Joa")
print(indice)

# Operador in para verificar se o valor está contido na string
texto = "Ana, Maria, Pedro, João, Joaquim"
print("Maria" in texto)

# Contar a quantidade de ocorrências
texto = "Ana, Maria, Pedro, João, Joaquim, Ana"
print(texto.count("Ana"))