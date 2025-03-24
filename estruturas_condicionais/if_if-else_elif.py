# "if" para criar estrutura condicional simples, composta por um único desvio


# Exemplo 1 
saldo = 2000.0
saque = float(input("informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")

# Exemplo 2
saldo = 2000.0
saque = float(input("Informe o valor do Saque"))

if saldo >= saque:
    print("Realizando saque!")

else:
    print("Saldo insuficiente!")

# "if/elif/else" cenários de mais de dois desvios.
# Exemplo 3

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe o valor para saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção Inválida!")

# Exemplo 4

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de Idade, pode tirara a CNH.")

# Exemplo 5
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

else:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")

elif idade == IDADE_ESPECIAL:
    print("Pode realizar aulas teóricas, mas não pode fazer aulas prática!")

else:
    print("Ainda não pode tirar a CNH.")    

