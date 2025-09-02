# Ler um ângulo qualquer e mostrar o seno, cosseno e tangente desse ângulo.
import math
ang = float(input("Digite o ângulo: "))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print(f"O valor em seno é {seno :.2f}°, em cosseno {cosseno :.2f}° e em tangente {tangente :.2f}°")