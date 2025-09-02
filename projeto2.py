# Simulando um Caixa Eletrônico

# O usuário tem um saldo iniciar de R$ 500 e pode sacar dinheiro até zerar o saldo ou encerrar

saldo = 500

while saldo > 0:
    saque = float(input("Informe o valor do saque(ou digite 0 para sair): "))
    if saque == 0:
        break

    if saque > saldo:
        print("Saldo insuficiente! Saque não efetuado")
    else:
        saldo -= saque
        print(f"Saque efetuado! Novo saldo R$ {saldo:.2f}")

print("Operação finalizada!")