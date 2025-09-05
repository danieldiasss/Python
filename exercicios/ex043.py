#  Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# – Abaixo de 18.5: Abaixo do Peso
# – Entre 18.5 e 25: c
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade mórbida
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura*altura)
print(f"O seu IMC é {imc :.2f}")
if imc < 18.5:
    print("Abaixo do Peso")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 40:
    print("Obesidade")
else:
    print("Obesidade mórdida")
    