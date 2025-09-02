#Contando de 1 a 5 com o FOR
# for numero in range (1,11):
#     print(numero)
# O range (1,11) gera os número de 1 a 10, o último número do range não é incluído

# compras = ["Arroz", "Feijão", "Batata", "Cenoura"]
# for item in compras: 
#     print(f"Comprar: {item}")

# palavra = "Python"
# for letra in palavra:
#     print(letra)

# contador = 5
# while contador > 0:
#     print(contador)
#     contador -= 1 #Diminui 1 do contador a cada repetição

# print("Fogo!!!")

senha_correta = "1234"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha:")

print("Acesso permitido")