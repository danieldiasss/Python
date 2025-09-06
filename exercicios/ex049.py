# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora faça utilizando o for

multiplo = int(input("Digite seu número: "))
print(f"A tabuada de {multiplo} é:")
for tabuada in range (0,11):
    print(f"{multiplo * tabuada}")
