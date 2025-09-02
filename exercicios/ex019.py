# Um professor quer sortear um dos seus alundos para apagar o quadro. Faça um programa
# que ajude ele lendo o nome deles e escrevendo o nome do escolhido

import random
alunos = ["Daniel", "Mirelly", "João", "Pedro"]
escolhido = random.choice(alunos)
print(f"O aluno sorteado é {escolhido}")