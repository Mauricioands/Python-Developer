texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()



# "FOR" com "RANGE"
 # Ex2
for numero in range(0, 11):
    print(numero, end=" ")

# Ex3
for numero in range(0,51,5):
    print(numero, end=" ")
