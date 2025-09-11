# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('cachorro', 'gato', 'passaro', 'peixe', 'leao', 'tigre', 'elefante')

for p in palavras:
    print(f"\nA palavra {p} possui as vogais: ", end="")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=" ")
