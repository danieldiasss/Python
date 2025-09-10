#  Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicit


while True:
    num = (int(input("Quer ver qual tabuada? [Negativo para parar: ")))
    if num < 0:
        break
    c = 0
    while c < 10:
        c += 1
        tabuada = num * c
        print(f"{c} x {num}: {tabuada}") 
print("Programa finalizado")