import os
os.system('cls')

numeros = [12,7,9,20,31,44,18,5]

par = 0
impar = 0

print("===== Números pares e impares =====")
for lista in numeros:
    if lista % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Números par: {par}")
print(f"Números impar: {impar}")