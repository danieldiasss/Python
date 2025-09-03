#print("\033[1;31;43m Olá, Mundo \033[m")
nome = "Daniel"
cores = {"limpa" : "\033[m" ,
          "azul": "\033[34m" ,
          "amarelo": "\033[33m" ,
          "pretoebranco" : "\033[7;30m"}
# print("Olá! Muito prazer em te conhecer,{}{}{}!!!" .format("\033[4;34m", nome , "\033[m"))
print("Olá! Muito prazer em te conhecer,{}{}{}!!!" .format(cores["amarelo"], nome, cores["limpa"]))