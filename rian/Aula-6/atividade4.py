import os,time
os.system('cls')

lista_notas = []

while True:

        try:
            print("===== Boletim =====")
            for lista in range(3):
                    nota = float(input(f"Digite a {lista+1}º nota: "))
                    if (nota>=0 and nota<=10):
                        lista_notas.append(nota)
                    else:
                        while True:
                            nota = float(input("Nota fora do permitido. Digite uma nota válida: "))
                            if (nota>=0 and nota<=10):
                                lista_notas.append(nota)
                                break

            for i in lista_notas:
                    media = (lista_notas[0] + lista_notas[1] + lista_notas[2]) / len(lista_notas)
                    if (media >= 7):
                        print(f"Aprovado!! média: {media:.1f}")
                    elif (media >=5 and media <=6.9):
                        print(f"Recuperação!! média: {media:.1f}")
                    else:
                        print(f"Reprovado!! média: {media:.1f}")
                    break
            break

        except:
            print("O número ou o valor inserido está incorreto!!")
            time.sleep(2)
            os.system('cls')