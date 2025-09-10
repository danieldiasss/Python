# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.

# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = (
    "Arroz", 10.50,
    "Feijão", 8.30,
    "Macarrão", 5.20,
    "Óleo", 7.00,
    "Açúcar", 4.80
)

print("-"*40)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print("-"*40)

for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f"{produtos[pos]:.<30}" , end ='')
    else:
        print(f"R${produtos[pos]:>7.2f}")
print("-"*40)