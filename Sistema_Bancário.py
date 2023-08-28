menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou, o valor digitado é inválido.")


    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou. Saldo insuficiente!!!")
        elif excedeu_limite:
            print("Operação falhou. O valor informado está acima do seu limite!!!")
        elif excedeu_saques:
            print(f"Operação falhou. Você excedeu o valor máximo de {LIMITE_SAQUES} diários.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            ("Operação falhou. O valor informado é inválido")

    elif opcao == "e":
        print("Extrato".center(48, "#"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("".center(48, "="))


    elif opcao == "q":
        
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
     