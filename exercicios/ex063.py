# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex:
# 0→1→1→2→3→5→8
print("Gerador de FIBONNACI")
print("=" *30 )
n = int(input("Digite um número:"))

primeiro = 0
segundo = 1
cont = 0

while cont < n:
    print(f"{primeiro} --> " , end = "")
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo
    cont += 1

    
print("Fim")