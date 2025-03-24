curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

ex1 = curso is nome_curso
print(ex1)

ex2 = curso is not nome_curso
print(ex2)

ex3 = saldo is limite
print(ex3)


saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)