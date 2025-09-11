# Crie um programa onde o usuário digita uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expres = str(input("Digite a expressão: "))
pilha = list
for simb in expres:
    if simb == "(":
        pilha.append("(")

    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop
        else:
            pilha.append(")")
            break
if len (pilha) == 0:
    print("Sua expressão está válida!")
else:
    print("Sua expressão está inválida!")