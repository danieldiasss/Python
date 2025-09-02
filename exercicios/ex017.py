# Ler o comprimento do cateto oposto e do adjacente de um triângulo retângulo e retorne
# o cumprimento da hipotenusa
# import math (pode fazer assim, basta colocar .hypot)
from math import hypot
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
# hi = (co**2 + ca**2) ** (1/2)
hi = hypot(co,ca)
print(f"Hipotenusa é igual a {hi :.2f}")

