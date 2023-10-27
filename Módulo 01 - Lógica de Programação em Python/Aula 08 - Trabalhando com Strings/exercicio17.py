import re

# Solicitar ao usuário para inserir o texto
texto = input("Digite o texto que contém CPFs: ")

# Encontraando os CPF
cpfs = re.findall(r'\d{11}', texto)

# Imprimir CPFs formatados
for cpf in cpfs:
    if len(cpf) == 11:
        cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        print(f"{cpf_formatado} é válido")
