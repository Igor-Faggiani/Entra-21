book = input("Informe o título do livro: ")
pg = int(input("Infrome a quantidade de páginas deste mesmo livro: "))

read_time = float(input("Informe o tempo médio para ler uma única página do livro, (em minutos): ")) * 60
read_time_day = float(input("Informe o tempo que tu dedica numa leitura diária, (em minutos): ")) * 60


pg_per_day = read_time_day / read_time
rating_calc = pg * read_time
complete_time_hour = rating_calc / 3600
complete_time_day = rating_calc / 86400
complete_time_week = rating_calc / 608400

print(f"Tendo em mente que com a quantidade de páginas lidas por dia sendo por volta de {pg_per_day} o tempo necessário para ler o livro será de: ")
print(f"- Em horas: {complete_time_hour:.3f} horas")
print(f"- Em dias: {complete_time_day:.3f} dias")
print(f"- Em semana: {complete_time_week:.3f} semanas")
