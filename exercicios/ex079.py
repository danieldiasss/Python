# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    num = float(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
    else:
        print("Valor já existe na lista. Não será adicionado.")
    continuar = str(input("Deseja continuar [S/N]: ")).strip().upper()[0]
    if continuar == "N":
        break
    
print(f"A lista com valores únicos e em ordem crescente é {lista}")