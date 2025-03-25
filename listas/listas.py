# Listas são mutáveis, portanto podemos alterar seus valores após a criação.
# "list" "["teste", "teste", "teste2"]"

frutas = ["laranja", "maçã", "uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["Ferrari", "F8", 420000, 2900, 2020, 'São Paulo', True]

# Matriz

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

# Fatiamento

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:]
lista[:2]
lista[1:3]
lista[0:3:2]
lista[::]
lista[::-1]


# enumerate

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carros}")


# Compreensão de listas

numeros = [1, 30, 21, 2 , 9 , 65, 34, 100]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

numeros = [1, 30, 21, 2 , 9 , 65, 34, 100, 120]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)


