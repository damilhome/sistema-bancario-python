menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito ----- R$ {valor:.2f}\n"
        return saldo, extrato, f"\nDepósito de R$ {valor} realizado."
    else:
        return "Valor inválido."

def sacar(saldo, numero_saques, extrato, valor, limite, LIMITE_SAQUES):
    if saldo >= valor:
        if valor <= limite:
            if numero_saques < LIMITE_SAQUES:
                saldo -= valor
                numero_saques += 1
                extrato += f"Saque -------- R$ {valor:.2f}\n"
                return saldo, numero_saques, extrato, f"\nSaque de R$ {valor:.2f} realizado"
            else:
                return saldo, numero_saques, extrato, "\nVocê já atingiu o limite de saques diários (3 saques)."
        else:
            return saldo, numero_saques, extrato, "\nValor acima do limite de saque (R$ 500.00)."
    else:
        return saldo, numero_saques, extrato, "\nSaldo insuficiente."

def exibir_extrato(saldo, extrato):
    if not extrato:
        extrato = "Não foram realizadas movimentações.\n"
    extrato += f"\nSaldo atual: R$ {saldo:.2f}"
    return extrato

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Digite o valor para depositar: "))
        saldo, extrato, mensagem = depositar(saldo, extrato, valor)
        print(mensagem)
    elif opcao == "s":
        valor = float(input("Digite o valor para sacar: "))
        saldo, numero_saques, extrato, mensagem = sacar(saldo, numero_saques, extrato, valor, limite, LIMITE_SAQUES)
        print(mensagem)
    elif opcao == "e":
        print(exibir_extrato(saldo, extrato))
    elif opcao == "q":
        break
    else:
        print("\nOperação inválida. Por favor, selecione novamente a operação desejada.")