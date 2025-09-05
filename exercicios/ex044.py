# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal
# – 3x ou mais no cartão: 20% de juros

# valor = int(input("Digite o valor do produto: "))
# cond_pag = str(input("Digite a forma de pagamento : ")).capitalize().strip()

# if cond_pag in ["Dinheiro", "Cheque"]:
#     print("Pagamento em dinheiro/cheque tem 10% de desconto.")
#     print(f"O valor a ser pago será {valor*0.9}")

# elif cond_pag == "Cartão a vista":
#     print("Pagamento no cartão à vista tem 5% de desconto.")
#     print(f"O valor à ser pago será {valor* 0.95}")

# elif cond_pag in ["2x","2 vezes", "duas vezes"]:
#     print("Pagamento em 2x no cartão não tem alteração de preço.")
#     print(f"O valor a ser pago será {valor}")

# else:
#     print("Pagamento em 3x ou mais tem 20% de juros.")
#     print(f"O valor a ser pago será {valor*1.2}")

print(f"{'Loja do Cruzdiro':=^40}")
valor = int(input("Digite o valor do produto: "))
print(''' FORMAS DE PAGAMENTO
[1] À vista dinheiro / cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input("Qual é a opção? "))

if opcao == 1:
    print("Pagamento em dinheiro/cheque tem 10% de desconto.")
    print(f"O valor a ser pago será {valor*0.9}")
elif opcao == 2:
    print("Pagamento no cartão à vista tem 5% de desconto.")
    print(f"O valor à ser pago será {valor* 0.95}")
elif opcao == 3:
     total = valor
     parcela = valor / 2
     print("Pagamento em 2x no cartão não tem alteração de preço.")
     print(f"O valor total a ser pago será {total}, e o valor parcelado será {parcela}")
elif opcao == 4:
    total = valor * 1.2
    total_parcelas = int(input("Quantas parcelas? "))
    parcela = total / total_parcelas
    print("Pagamento em 3x ou mais tem 20% de juros.")
    print(f"O valor total a ser pago será {total}, e o valor parcelado será {parcela :.2f}.")
else:
    "Opção inválida de pagamento. Tente novamente"