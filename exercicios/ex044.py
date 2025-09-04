# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal
# – 3x ou mais no cartão: 20% de juros

valor = int(input("Digite o valor do produto: "))
cond_pag = str(input("Digite a forma de pagamento : ")).capitalize().strip()

if cond_pag in ["Dinheiro", "Cheque"]:
    print("Pagamento em dinheiro/cheque tem 10% de desconto.")
    print(f"O valor a ser pago será {valor*0.9}")

elif cond_pag == "Cartão a vista":
    print("Pagamento no cartão à vista tem 5% de desconto.")
    print(f"O valor à ser pago será {valor* 0.95}")

elif cond_pag in ["2x","2 vezes", "duas vezes"]:
    print("Pagamento em 2x no cartão não tem alteração de preço.")
    print(f"O valor a ser pago será {valor}")

else:
    print("Pagamento em 3x ou mais tem 20% de juros.")
    print(f"O valor a ser pago será {valor*1.2}")