# o mesmo professor quer sortear a ordem de apresentação dos alunos. Fazer um programa
# que leia o nome dos quatros alunos e mostra a ordem sorteada
import random
alunos = ["Daniel","Mirelly","João","Pedrin"]
random.shuffle(alunos)

print(f"A ordem de apresentação será {alunos}")