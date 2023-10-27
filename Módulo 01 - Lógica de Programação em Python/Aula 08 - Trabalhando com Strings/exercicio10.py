texto = input('Escreva um texto: ').lower()

#dividir o texto em palavras (LISTA)
palavras = texto.split()

#Remover Duplicatas
palavras_unicas = set(texto)

#Contar o numero de palavras unicas
cont_palavras = len(palavras_unicas)

print(f'O numero de palvras únicas do texto é de: {cont_palavras}')


