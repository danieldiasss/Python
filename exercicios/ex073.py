# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Cruzeiro.
times = [
    "Flamengo",
    "Cruzeiro",
    "Palmeiras",
    "Bahia",
    "Botafogo",
    "Mirassol",
    "São Paulo",
    "Red Bull Bragantino",
    "Fluminense",
    "Internacional",
    "Ceará",
    "Corinthians",
    "Grêmio",
    "Atlético Mineiro",
    "Vasco da Gama",
    "Santos",
    "Vitória",
    "Juventude",
    "Fortaleza",
    "Sport"
]

print(f"Os 5 primeiros colocados são {times[0:5]}")
print(f"O G4 é {times[0:4]}")
print(f"Os times em ordem alfabética são {sorted(times)}")
print(f"O Cruzeiro está localizado em {times.count("Cruzeiro" )+1} lugar")