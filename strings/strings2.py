# "f-string"
nome = "Maurício"
idade = 34
profissão = "Analista de Sistemas"
linguaguem = "Python"

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade {0}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))

print(f"Nome = {nome} Idade = {idade}")