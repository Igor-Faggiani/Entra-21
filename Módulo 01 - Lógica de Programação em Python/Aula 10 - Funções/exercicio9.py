def mostrar_informacoes(**info):
    """Função para mostrar informações formatadas."""
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

mostrar_informacoes(nome="João", idade=25, cidade="São Paulo")
mostrar_informacoes(profissao="Engenheiro", salario=5000)
