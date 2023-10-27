def formata_cpf(numero):
    # Verificar se o número é um inteiro
    if not isinstance(numero, int):
        return str(numero)  # Se não for um inteiro, retorna o número como string

    # Verificar se o número possui 11 dígitos (tamanho de um CPF válido)
    numero_str = str(numero)
    if len(numero_str) != 11:
        return numero_str  # Se não tiver 11 dígitos, retorna o número como string

    # Formatar o número no formato de CPF
    cpf_formatado = f"{numero_str[:3]}.{numero_str[3:6]}.{numero_str[6:9]}-{numero_str[9:]}"
    return cpf_formatado


cpf1 = 12345678901
cpf2 = "12345678901"
cpf3 = 12345

cpf_formatado1 = formata_cpf(cpf1)
cpf_formatado2 = formata_cpf(cpf2)
cpf_formatado3 = formata_cpf(cpf3)

print(cpf_formatado1)
print(cpf_formatado2)
print(cpf_formatado3)
