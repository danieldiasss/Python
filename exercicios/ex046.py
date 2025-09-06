# Faça um programa que mostre na tela uma contagem
# regressiva para o fogo de artificio indo de 10
# a 0 com uma pausa de 1 segundo entre eles
import time

print("=" *30 )
print("Contagem regressiva")
for contar in range (10,-1,-1):
    time.sleep(1)
    print(contar)
print("FOGOS!!!!")