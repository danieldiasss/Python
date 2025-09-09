# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário 
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e 
# qual foi a soma entre eles (desconsiderando o flag).
print("SOMA DE VÁRIOS NÚMEROS")
print("-=-" *30 )

num = 0
valor = 0
cont = 0
print("Digite 999 para sair")
print("-=-" *30 )
valor = int(input("Digite um número: "))
while valor != 999:
    valor = int(input("Digite um número: "))
    num = num + valor
    cont += 1
print(f"A soma dos números foi {num} e o total de números foi {cont}")