# Crie um programa que mostre todos os números pares de um intervalo de 1 e 50
s = 0
for pares in range (2,51,2):
    s += pares
    print(pares)
print("A soma dos números é {}" .format(s))