import os
os.system('cls')
import time

lista_tarefas = []
quantidadeTarefa = False

while True:
    print("===== Gerenciamento de Tarefas =====")
    print("1 - Adicionar Tarefa")
    print("2 - Remover Tarefa")
    print("3 - Mostrar Tarefas")
    print("0 - Sair")
    escolha = int(input("Escolha: "))

    if escolha == 1:

        os.system('cls')
        print("===== Adicionando tarefa =====")
        tarefa = input("Digite qual tarefa deseja registrar: ")
        lista_tarefas.append(tarefa)
        print("Tarefa registrada...")
        quantidadeTarefa = True
        time.sleep(2)
        os.system('cls')

    elif escolha == 2:

        if not quantidadeTarefa:
            print("Adicione primeiro as tarefas")
            time.sleep(2)
            os.system('cls')

        else:
            os.system('cls')
            print("===== Lista de Tarefas Para Remover =====")
            print("\n".join(lista_tarefas))
            remover_tarefa = input("Digite qual tarefa deseja remover: ")

            if remover_tarefa in lista_tarefas:
                lista_tarefas.remove(remover_tarefa)
                print("Tarefa removida...")
                time.sleep(2)
                os.system("cls")
            else:
                print("Tarefa não encontrada...")
                time.sleep(2)
                os.system("cls")

    elif escolha == 3:

        if not quantidadeTarefa:
            print("Adicione primeiro as tarefas")
            time.sleep(2)
            os.system('cls')

        else:
            os.system('cls')
            print("===== Lista de Tarefas =====")
            print("\n".join(lista_tarefas))
            time.sleep(5)
            os.system("cls")

    elif escolha == 0:
        print("Sistema encerrado...")
        time.sleep(2)
        break

    else:
        print("Escolha inválida...")
        time.sleep(2)
        os.system('cls')

