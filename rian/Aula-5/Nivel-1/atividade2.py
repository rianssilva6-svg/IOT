import os
os.system('cls')

produtos = []

print("===== Sistema de Compra =====")
for lista in range(5):
    produto = input(f"Digite o {lista+1}º produto: ")
    produtos.append(produto)

quantidade = len(produtos)

print("\n")

print("===== Compras =====")
for compra in range(5):
    print(produtos[compra])

print(f"quantidade de produtos: {quantidade}")