frutas = ["maça", "banana", "laranja"]
numeros = [1,2,3,4,5]
misturada = ["Python", 3.14, True]

#Acessando elementos da lista
#[10,11,12,13]
#[posição 0, posição 1, posição 2, posição 3]
# print(frutas[0]) #maça
# print(frutas[1]) #banana
# print(frutas[2]) #laranja
# print(frutas[-1]) #laranja (índice negativo conta de trás para frente)

#Alterando um valor na lista
# frutas[1] = "uva"
# print(frutas)

#Adicionando elementos à lista

#append(): adiciona um item ao final da lista
#insert(): adiciona um item em uma posição específica

# numeros = [1,2,3]
# print(numeros)

# numeros.append(4)
# print(numeros) #[1,2,3,4]

# numeros.insert(1, 10) #(posição, valor)
# print(numeros) #[1,10,2,3,4]

# #Removendo elementos da lista

# remove(): remove um item pelo valor  
# pop(): remove um item pelo índice (ou o último item se nenhum índice for passado)

# frutas = ["maça", "banana", "laranja", "uva"]
# print(frutas)

# frutas.remove("banana")
# print(frutas)  #['Maça', 'laranja', 'uva']

# frutas.pop(0)
# print(frutas)  # ['laranja', 'uva']

# frutas.pop()
# print(frutas) #['laranja]

# tuplas

# tuplas são como listas, mas imutáveis. Elas são criadas com parênteses ().

# cores = ("vermelho", "azul", "verde")
# numeros = (1,2,3,4,5)

#Acessando elementos
# print(cores[0])  # 'vermelho'
# print(cores[-1]) # 'verde'

#Tentando modificar uma tupla (Erro!)
# cores[1] = "amarelo" #Isso gera um erro, pois tuplas são imutáveis

# Convertendo entre lista e tupla
# Podemos converter uma tupla para uma lista e modificar os elementos
tupla = (1,2,3)
lista = list(tupla)  #converte para lista
lista.append(4)
tupla = tuple(lista)   #converte de volta para tupla
print(tupla)   #1,2,3,4

# quando usar tuplas?
# Quando queremos garantir que os valores não sejam alterados
# Para armazenar dados fixos como coordenadas, meses do ano, dias da semana, etc.

meses= ("Janeiro", "Fevereiro", "Março", "Abril")
print(meses[2])  #Março
