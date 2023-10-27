valor_gb = float(input("Informe o tamanho do arquivo em GB: "))
para_mbyte = valor_gb * 1024
para_kbyte = (valor_gb * 1024)*1024
para_byte = ((valor_gb * 1024)*1024)*1024
para_bit = (((valor_gb * 1024)*1024)*1024)*1024

print(f"O tamanho do arquivo passado em GB para MB é de {para_byte}, em KB é de {para_kbyte}, em Byte é de {para_byte} e em bits é de {para_bit}.")
