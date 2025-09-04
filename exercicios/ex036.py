# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

emprestimo = int(input("Digite o valor do empréstimo? "))
salario = int(input("Digite o valor do seu salário: "))
anos = int(input("Digite em quantos anos tu vai pagar: "))
prestacao_mensal = emprestimo / (anos * 12)
min = salario * 0.3

print(f"O valor da prestação mensal é {prestacao_mensal :.2f} R$")
if min > prestacao_mensal:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")