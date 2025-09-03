# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("-=-"*20)
print("Analisador de triângulos")
print("-=-"*20)
a = float(input("Digite o primeiro segmento: "))
b = float(input("Digite o segundo segmento: "))
c = float(input("Digite o terceiro segmento: "))
print("Pode ser um triângulo" if a+b>c and a+c > b and b+c>a else "Não pode ser um triângulo")