menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
       
       valor = float(input("informe o valor do depósito: "))
       # Verifica se o valor do depósito não é menor que 0 (valor negativo)
       if valor > 0:
           saldo += valor
           extrato += f"Depósito: R$ {valor:.2f}\n"
           print("Depósito realizado com sucesso!")
       else:
           print("Operação falou! O Valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor para saque: "))

        # Verifica se o valor do saque é maior que o saldo em conta
        excedeu_saldo = valor > saldo
        # Verifica se o valor do saque é maior que o Limite em conta
        excedeu_limite = valor > limite
        # Verifica se o numero de saque ultrapassou o limite de 3 saques
        excedeu_saques = numero_saques >= LIMITE_SAQUES        
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiênte.")
        
        elif excedeu_limite:
            print("Operação falhou! O Valor do quese excede o limite")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")

        if valor > 0:
            saldo -= valor
            extrato += f"Saque no valor de R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado no valor de R$ {valor:.2f}")

        else:
            print("Operação falhou! O valor informado não é válido.")

    elif opcao == "e":
        print("\n================ EXTRATOS ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")

    elif opcao == "q":
        print("Obrigado por utilizar nossos serviços.")
        break
        

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
