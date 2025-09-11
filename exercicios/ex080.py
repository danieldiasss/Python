#  Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta da inserção
#  (sem usar o sort()).

# No final, mostre a lista ordenada na tela.
lista = []
cont = 0
while cont <5:
    num = int(input("Digite um número: "))
    lista.append(num)
    cont += 1