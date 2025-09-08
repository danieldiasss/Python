# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA. mostrando os 10 primeiros termos da progressão usando a estrutura while.
n1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
cont = 1
termo = n1
while cont <= 10:
    print(f" {termo} --> " , end = "")
    termo += r
    cont += 1
print("Fim")