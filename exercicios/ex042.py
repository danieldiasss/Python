# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – Equilátero: todos os lados iguais
# – Isósceles: dois lados iguais
# – Escaleno: todos os lados diferentes

lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))
if lado1+lado2>lado3 and lado1+lado3 > lado2 and lado2+lado3>lado1 :
    print("Podem formar um triângulo")
    if lado1 == lado2 == lado3:
        print("Esse triângulo é equilátero")
    elif lado1 != lado2 != lado3 != r1:
        print("Esse triângulo é escaleno")
    else:
        print("Esse trinângulo é isósceles")
else:
    print("Não podem formar um triângulo")