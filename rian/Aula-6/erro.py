import os
os.system('cls')

while True:
    try:
        idade = int(input("Digite a sua idade: "))
        if idade >=18:
            print("Maior de idade")
            break
        else:
            print("Menor de idade")
            break

    except:
        print("Dado inválido!! Somente números")