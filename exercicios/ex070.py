# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

print("-"*50)
print("MOSTRE A SUA COMPRA")
print("-"*50)

total = totmil = menor = cont = 0
barato = ' '
while True:
   produto = str(input("Qual o nome do produto?")).strip()
   valor = float(input("Qual o valor do produto? "))
   cont+=1
   if cont == 1 or valor < menor:
      menor = valor
      barato = produto
      
   total += valor
   if valor > 1000:
      totmil += 1

   continuar = ' '
   while continuar not in "SN":
      continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
   if continuar == "N":
      break

   print("-"*50)

print("Fim do programa")
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {totmil} produtos custando mais de R$1000")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")