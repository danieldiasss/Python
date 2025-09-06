# Faça um programa que calcule a soma de todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 e 500
s = 0
for n in range (1,501,2):
    if n % 3 == 0:
        s += n
print(f"A soma dos números ímpares no intervalo de 1-500 que dividem por 3 é {s}")