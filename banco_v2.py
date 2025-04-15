import textwrap

def menu(): 
    texto_menu = """

    --------- MENU ---------

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair

------------------
=> """
    return input(texto_menu)

def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} efetuado com sucesso!\n")
    else:
            print("Operação falhou! Informe um valor válido para depósito.\n")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    
    excedeu_saldo = valor > saldo
    excedeu_valor_limite = valor > limite
    excedeu_limite = numero_saques >= limite_saques

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


    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n--- Extrato ---")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("----------------------------\n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print("Já existe usuário com esse CPF!")
         return
    
    nome = input("Informe o seu nome completo:  ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):  ")
    endereco = input("Informe o seu endereço (logradouro, nro - bairro - cidade/sigla estado):  ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})

    print("--=-- Usuário criado com sucesso! --=--")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário:  ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
         print("\n --+-- Conta criada com sucesso! --+--")
         return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n ----- Usuário não encontrado, realize primeiro o cadastro! -----")

def listar_contas(contas):
    for conta in contas:
         linha = f"""
            Agencia: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
         print("="*100)
         print(textwrap.dedent(linha))
    return

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():

    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            print("\n--- Depósito ---")
            valor = float(input("Informe o valor que deseja depositar: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == "s":
            print("\n--- Saque ---")
            valor = float(input("Informe o valor que deseja sacar: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("Encerrando o sistema. Obrigado por utilizar nosso banco!\n")
            break

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
             numero_conta = len(contas) + 1
             conta = criar_conta(AGENCIA, numero_conta, usuarios)

             if conta:
                  contas.append(conta)



        elif opcao == "lc":
            listar_contas(contas)

        else:
            print("Operação inválida! Por favor, selecione uma opção válida.\n")

print("Bem-vindo ao Sistema Bancário!\n")

main()




