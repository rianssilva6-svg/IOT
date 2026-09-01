import os
os.system('cls')

lista_notas = []

while True:
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

    if nota < 0:
        quantidade = len(lista_notas)
        media = sum(lista_notas) / len(lista_notas)
        maior = max(lista_notas)
        menor = min(lista_notas)

        lista_notas.sort()
        lista_notas.reverse()

        print("\n")
        print("===== Resultado =====")
        print(f"A maior nota: {maior}")
        print(f"A menor nota: {menor}")
        print(f"A media de todas as notas: {media:.1f}")
        print(f"Ordem Decrescente: {lista_notas}")
        break