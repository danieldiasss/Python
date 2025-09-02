km_pecorridos = float(input("Quantos Km foram pecorridos? "))
diária = int(input("Quantos dias alugados? "))

print(f"O valor a ser pago será R${km_pecorridos * 0.15 + diária * 60 :.2f}.")
