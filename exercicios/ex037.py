# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal ''')

opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"{num} convertido para binário é igual a {bin(num)}")
elif opcao == 2:
    print(f"{num} convertido para octal é igual a {oct(num)}")
else:
    print(f"{num} convertido para hexadecimal é igual a {hex(num)}")