texto = input('Escreva um texto de no máximo 20 caractéres: ')

if len(texto) > 20:
    texto_abreviado = texto[:20 - 3] + "..."
    print(texto_abreviado)
else:
    print("O texto não excede o limite de caracteres.")
    
