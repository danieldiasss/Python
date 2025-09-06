# for c in range (1,11):
#     print(c)
# print("FIM")

# Fazendo o mesmo programa com While
# c=1
# while c < 11:
#     print(c)
#     c +=1
# print("Fim")

# Fazendo soma de valores infinitos
'''valor = 0
r = "S"
while r == "S":
    val = int(input("Digite um valor: "))
    valor += val
    r = str(input("Quer continuar? [S/N]")).upper()
    
print("FIM")
print(f"A soma dos valores é {valor}")'''

# Mostrando quantos ímpares e pares digitou
n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print(f"Você digitou {par} números pares e {impar} números ímpares.")
