# # Listas são entre colchetes[], enquanto as tuplas entre parênteses ()
# # Listão são mutáveis
# num = [2,5,9,1]
# num[2] = 3   # troca elemento de uma lista
# num.append(7) # adiciona elemento à uma lista
# num.sort()   # deixa de forma crescente
# num.sort(reverse=True)  # deixa de forma decrescente
# num.insert(2,0)  # na posição irá inserir o 0
# num.pop()   # elimina o último valor
# num.pop(3)  # elimina o 3 elemento da lista que 
# num.remove(2) # elimina o primeiro valor 2 da lista, se não tiver o valor da lista dá erro

# print(num)
# print(f"Essa lista tem {len(num)} elementos")



# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for c, v in enumerate(valores):     # c é a chave(onde está localizada)   v é o valor (1,2,3,4,5,6.....)
#     print(f'Na posição {v} encontrei o valor {c}')
# print("Cheguei ao final da lista")



# valores = list()
# for cont in range (0,5):
#     valores.append(int(input("Digite um valor: ")))
# for c, v in enumerate(valores):
#     print(f"Na posição {c} encontrei o valor {v}")
# print("="*30)
# print("Cheguei ao final da lista")

# a = [2,3,5,7]
# b = a
# b[2] = 8           
# print(f"Lista {a}")
# print(f"Lista {b}")       # a partir do momento que você iguala uma lista na outra, as duas ficam ligadas

# a = [2,3,5,7]
# b = a [:]             # faz uma cópia
# b[2] = 8           
# print(f"Lista {a}")
# print(f"Lista {b}") 


# teste = list()
# teste.append('Daniel')
# teste.append(40)

# galera = list()
# galera.append(teste[:])

# teste [0] = 'Maria'
# teste [1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [['Joao', 19] , ['Ana' , 33] , ['Joaquim' , 13] , ['Maria', 45]]
# print(galera[2] [1])

# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmai = totmen = 0
for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1]>= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f"Temos {totmai} maiores e {totmen} menores de idade")