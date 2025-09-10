# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:

# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato.

print("-"*50)
print("MOSTRE A SUA COMPRA")
print("-"*50)

barato = None
total = produtos_caros = 0
while True:
   produto = str(input("Qual o nome do produto?")).strip()
   valor = int(input("Qual o valor do produto? "))
   continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
   print("-"*50)

   total += valor
   if valor > 1000:
      produtos_caros += 1

   if continuar == "N":
      break
   
   if barato is None or valor < barato:
      barato = valor
      nome_barato = produto
   
   
print("-"*50)
print(f'''
      O total gasto é {total}
      Existem {produtos_caros} produtos que custam mais de R$1000.
      O produto mais barato é {nome_barato}
      
''')
print("-"*50)