# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – Equilátero: todos os lados iguais
# – Isósceles: dois lados iguais
# – Escaleno: todos os lados diferentes

lado1 = float(input("Digite o valor do primeiro lado: "))
lado2 = float(input("Digite o valor do segundo lado: "))
lado3 = float(input("Digite o valor do terceiro lado: "))

if lado1 == lado2 == lado3:
    print("Esse triângulo é equilátero")
elif lado1 == lado2 != lado3:
    print("Esse triângulo é isósceles")
elif lado3 == lado1 != lado2:
    print("Esse triângulo é isósceles")
else:
    print("Esse trinângulo é escaleno")