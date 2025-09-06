# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#  frase que de frente pra trás e vice versa é a mesma coisa
# frase = str(input("Digite uma frase: ")).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''

# for letra in range (len(junto) -1,-1,-1):
#     inverso += junto[letra]
# print(f"O inverso de {junto} é {inverso}")
# if inverso == junto:
#     print("Temos um palíndromo!")
# else:
#     print("Não temos um palíndromo!")



frase = str(input("Digite uma frase: ")).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(f"O inverso de {junto} é {inverso}")

if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("Não temos um palíndromo!")
