import os
os.system('cls')

print("===== Números =====")

numeros = []

for lista in range(6):
    num = int(input(f"Digite o {lista+1}º número: "))
    numeros.append(num)

soma = sum(numeros)
maior_valor = max(numeros)
menor_valor = min(numeros)
numeros.sort()


print("===== Resultado =====")
print(f"O maior valor é: {maior_valor}")
print(f"O menor valor é: {menor_valor}")
print(f"A soma dos valores é de: {soma}")
print(f"Ordem Crescente: {numeros}")