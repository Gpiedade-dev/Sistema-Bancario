# PROJETO BANCARIO DIO
# OBS: tentei fazer algo diferente para ir treinando um pouco mais , pois estou trabalhando em outro projeto parecido!

def menu():
    return input("""
===== MENU =====
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=================
Escolha: """).lower()


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(" Depósito realizado com sucesso!")
    else:
        print(" Operação falhou! Valor inválido.")
    return saldo, extrato


def sacar(saldo, extrato, valor, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print(" Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(" Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print(" Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(" Saque realizado com sucesso!")
    else:
        print(" Operação falhou! Valor inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato, numero_saques):
    print("\n************** EXTRATO **************")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("*************************************")
    print(f"Número de saques realizados hoje: {numero_saques}")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = menu()

    if opcao == "1":
        try:
            valor = float(input("Informe o valor do depósito: "))
        except ValueError:
            print(" Digite um número válido.")
            continue
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "2":
        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError:
            print(" Digite um número válido.")
            continue
        saldo, extrato, numero_saques = sacar(
            saldo, extrato, valor, limite, numero_saques, LIMITE_SAQUES
        )

    elif opcao == "3":
        exibir_extrato(saldo, extrato, numero_saques)

    elif opcao == "0":
        print(" Saindo... obrigado por usar o sistema bancário!")
        break

    else:
        print(" Opção inválida. Escolha: 1 / 2 / 3 / 0.")