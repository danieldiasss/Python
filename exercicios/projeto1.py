# Jogo de advinhação

# No jogo, o usuário precisa advinhar um número secreto.
# Ele pode tentar várias vezes até acertar.

numero_secreto = 5
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Tente advinhar um número de 1 a 20:"))
    
    if tentativa < numero_secreto:
        print("O número é secreto é maior")
    elif tentativa > numero_secreto:
        print("O número é menor")
    else:
        print("Parabéns,você acertou")
