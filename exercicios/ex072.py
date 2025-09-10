# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero_extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze' , 'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num =int(input("Digite um número de 0 a 20: "))
    if num not in range (21):
        num =int(input("Digite um número de 0 a 20: "))
    else:
        break

print(f"O número em extenso é {numero_extenso[num]}.")