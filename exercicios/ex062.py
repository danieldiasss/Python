#  Melhora o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
print("GERADOR DE PROGRESSÃO ARITMÉTICA")
print("-=-" *20)
n1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

total = 0
mais = 10
termo = n1
cont = 1
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo}--> " , end = "" )
        cont += 1
        termo += razao
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar mais? "))
print("Fim")