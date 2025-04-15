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
        print("\n--- Depósito ---")
        valor = float(input("Informe o valor que deseja depositar: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} efetuado com sucesso!\n")
        else:
            print("Operação falhou! Informe um valor válido para depósito.\n")

    elif opcao == "s":
        print("\n--- Saque ---")
        valor = float(input("Informe o valor que deseja sacar: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_valor_limite = valor > limite
        excedeu_limite = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.\n")
        elif excedeu_valor_limite:
            print("Operação falhou! Valor acima do limite por saque.\n")
        elif excedeu_limite:
            print("Operação falhou! Número máximo de saques diários atingido.\n")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!\n")
        else:
            print("Operação falhou! Informe um valor válido.\n")

    elif opcao == "e":
        print("\n--- Extrato ---")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("----------------------------\n")

    elif opcao == "q":
        print("Encerrando o sistema. Obrigado por utilizar nosso banco!\n")
        break

    else:
        print("Operação inválida! Por favor, selecione uma opção válida.\n")
