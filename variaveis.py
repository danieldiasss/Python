nome = "Daniel"
idade = 19
altura = 1.79
dev= False

#print(f"Olá, {nome}Você tem {idade} anos e mede {altura}m.")

nome = input("Digite seu nome:") #entrada de texto  
idade = int(input("Digite sua idade:")) #entrada de texto convertidada para int
altura = float(input("Digite sua altura")) #entrada de texto convertidada para float

print(f"Olá, {nome}! Você tem {idade} e mede {altura}m.")