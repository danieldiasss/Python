# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print("="*30)
print("ÍMPAR OU PAR")
print("="*30)

vitorias = 0
derrotas = 0
while True:
    if derrotas == 1:
        break
    
    jogo = int(input("Digite um número: "))
    impar_par = str(input("ÍMPAR ou PAR? [I/P]: ")).strip().upper()[0]
    
    computador = randint(0,5)
    total = computador + jogo

    if total % 2 == 0 and impar_par == "P":
        print(f"Eu joguei {computador} e você {jogo} e o total foi {total}. Deu par,você ganhou!!!")
        vitorias += 1
        print("="*30)

    elif total % 2 == 1 and impar_par == "I":
        print(f"Eu joguei {computador} e você {jogo} e o total foi {total}. Deu ímpar, você ganhou!!!")
        vitorias += 1
        print("="*30)

    if total % 2 == 0 and impar_par == "I":
        print(f"Eu joguei {computador} e você {jogo} e o total foi {total}. Deu par, você perdeu")
        derrotas += 1
        print("="*30)

    elif total % 2 == 1 and impar_par == "P":
        print(f"Eu joguei {computador} e você {jogo} e o total foi {total}. Deu ímpar, você perdeu")
        derrotas += 1
        print("="*30)
        
print(f"Você ganhou {vitorias}x.")