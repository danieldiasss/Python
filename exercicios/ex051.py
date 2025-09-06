 # Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostres os 10 primeiros termos dessa progressão.
primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

print("O resultado dos 10 primeiros termos é: ")
# pa = primeiro_termo (n-1). razao
for c in range (0,10):
    print (primeiro_termo + (c) * razao , end = " ")