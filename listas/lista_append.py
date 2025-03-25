lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

lista = [1, "Python", [40, 30, 20]]
l2 = lista.copy()

print(lista)

print(id(l2), id(lista))

l2[0] = 2

print(l2)
print(lista)


# count

cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho")
cores.count("azul")
cores.count("verde")


# extend

linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])
print(linguagens)


# pop

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop()
linguagens.pop()
linguagens.pop(0)

#remove

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)


# reverse

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()
print(linguagens)

# sort

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x:len(x))

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x:len(x), reverse=True)

# len

linguagens = ["python", "js", "c", "java", "csharp"]
len(linguagens)

# sorted

linguagens = ["python", "js", "c", "java", "csharp"]
sorted(linguagens, key=lambda x: len(x))

sorted(linguagens, key=lambda x: len(x), reverse=True)