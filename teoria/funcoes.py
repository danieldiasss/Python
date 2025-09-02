#Funções

#Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Em vez de escrever o mesmo código várias vezes, criamos uma função e apenas a chamamos sempre que necessário
#Exemplo real
# Imagine que você tem que calcular o imposto de
# vários produtos em uma loja. Em vez de repetir 
# tudo, você pode criar uma função chamada 
# calcular_imposto() e usá-la sempre que precisar.

# def <nome da funcao> ():
    # Precisa estar tudo indetado (espaçozinho)

# def saudacao(nome):
#     print(f"Olá,{nome}! Bem vindo ao curso de Python.")

# saudacao("Maria")

# Retorno de valores        
# def somar (a,b):
#     return a + b

# # Chamando a função e armazenando o resultado
# resultado = somar (5, 7)
# print(f"A soma é {resultado}")

# Função com vários parâmetros

def calcular_media(n1,n2,n3):
    media = (n1 + n2 + n3) / 3
    return media

# Chamando a função
resultado = calcular_media(8,9,9)
print(f"A média é {resultado :.2f}")