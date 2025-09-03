# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a R$1.250,00, calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input("Digite seu salário: "))
if salario <= 1250:
    print("O seu novo salário é {:.2f}" .format(salario + salario *0.15))
else:
    print("O seu novo salário é {:.2f}" .format(salario + salario * 0.10))