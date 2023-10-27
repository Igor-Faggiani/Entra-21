"""
16. Dado dois dicionários, encontre as chaves que estão presentes em apenas um dos dicionários.
"""
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 2, "c": 4, "d": 5}

# Tranformar as chaves em um conjunto
chaves_dict1 = set(dict1.keys())
chaves_dict2 = set(dict2.keys())

# Encontrar a diferença simétrica
chaves_exclusivas = chaves_dict1.symmetric_difference(chaves_dict2)
print(chaves_exclusivas)
