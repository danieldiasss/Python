# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
números_aleatórios = []
cont = 0
while cont <5:  
    números = randint(1,10)
    cont += 1
    números_aleatórios.append(números)

números_aleatórios.sort()

print(números_aleatórios)
print(f"O menor número é {números_aleatórios[0]}")
print(f"O maior valor é {números_aleatórios[4]}")