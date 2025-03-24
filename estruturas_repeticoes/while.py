opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato \n[3] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar o nosso sistema bancário, até logo!")


# "break"

while True:
    numero = int(input("Informe o número: "))

    if numero == 10:
        break
    
    print(numero)