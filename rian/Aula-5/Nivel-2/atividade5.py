import os
os.system('cls')

lista_nomes = []

while True:
    print("===== Lista de nomes =====")
    print("1 - Cadastrar nomes")
    print("2 - Sair")
    escolha = int(input("Escolha: "))

    if escolha == 1:
        nome = input("Digite o nome do convidado: ")
        lista_nomes.append(nome)
        os.system('cls')

    elif escolha == 2:
        print("===== Resultado =====")
        lista_nomes.sort()
        print(f"Nomes: {lista_nomes}")
        print(f"Quantidade de convidados: {len(lista_nomes)}")
        break