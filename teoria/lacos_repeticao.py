# Laço com variável de Controle

# # contando várias vezes
# for c in range (1,6):
#     print("Oi")
# print("FIM")

# # contar para trás
# for c in range (6,0, -1):
#     print("c")
# print("FIM")


# # Contando de 1 em 1
# n = int(input("Digite um número: "))
# for c in range (0,n + 1):
#     print (c)
# print("Fim")

# # Contando de acordo com o passo,inicio e fim
# i = int(input("Início: "))
# f = int(input("Fim: "))
# p = int(input("Passo: "))
# for c in range (i,f+1, p):
#     print(c)
# print("Fim")

# Fazendo um somatório de números

s = 0
for c in range (0,4):
    n = int(input("Digite um número: "))
    s +=  n
print(f"O somatório de todos números é {s}")
