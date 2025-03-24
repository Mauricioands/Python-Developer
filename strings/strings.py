curso = "pYtHon"
# Converte todos os carecteres para maiusculo
print(curso.upper())

# Converte todos os caracteres para minusculo
print(curso.lower())

# Primeira letra maiuscula e o restante minusculo.
print(curso.title())

curso = "    Python  "

# Cortar os espaços em branco "strip"
print(curso.strip())

# Cortar espaço em braco a esquerda
print(curso.lstrip())

# Cortar espaço em branco a direita
print(curso.rstrip())


menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))