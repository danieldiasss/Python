

#Sintaxe básica no Python
# if - se   
# else - se não
# elif - se + se não

#if condição:    
    # código a ser executado se a condição for verdadeira
#elif outra_condição:
    # Código executado se a primeira condição for falsa, mas essa verdadeira
#else:
    # Código executado se nenhuma das condições anteriores for verdadeira


# Verificando a idade para entrada em um evento (18 anos)
# idade = int(input("Digite sua idade"))

# if idade >= 18:
#     print("Você pode ir")
# else: 
#     print("Você não pode ir")

nota = float(input("Digite sua nota: "))
if nota >= 7:
     print ("Você foi aprovado")
elif nota >= 5: 
    print ("Você irá para a recuperação")
else:
     print("Você foi reprovado")