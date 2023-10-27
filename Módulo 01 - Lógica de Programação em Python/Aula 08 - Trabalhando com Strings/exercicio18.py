import re

texto = input("Digite o texto que contém CPFs: ")

# Encontrando todos os CPF
cpfs = re.findall(r'\d{11}', texto)

# Validar e formatar CPFs válidos
for cpf in cpfs:
    if len(cpf) == 11:
        # Calcular o primeiro dígito verificador
        soma = 0
        peso = 10
        for digit in cpf[:9]:
            soma += int(digit) * peso
            peso -= 1
        resto = soma % 11
        if resto < 2:
            digito1 = 0
        else:
            digito1 = 11 - resto

        # Calcular o segundo dígito verificador
        soma = 0
        peso = 11
        for digit in cpf[:10]:
            soma += int(digit) * peso
            peso -= 1
        resto = soma % 11
        if resto < 2:
            digito2 = 0
        else:
            digito2 = 11 - resto

        # Verificar se os dígitos verificadores são válidos
        if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            print(f"{cpf_formatado} é válido")
