import os
os.system('cls')

positivo = []
negativo = []

print("===== Lista de 10 números positivos e negativos =====")
for count in range(10):
    num = int(input(f"Digite o {count+1}º número: "))

    if num >= 0:
        positivo.append(num)
    else:
        negativo.append(num)
        
soma = sum(positivo)
quant_positivo = len(positivo)
quant_negativo = len(negativo)

print(f"Quantidade de números positivos: {quant_positivo}")
print(f"Quantidade de números negativos: {quant_negativo}")
print(f"Vetor de números negativos: {negativo}")
print(f"Soma de números positivos: {soma}")