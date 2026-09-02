import os,time
os.system('cls')

while True:
    try:
        print("===== Verificação de idade =====")
        idade = int(input("Digite sua idade: "))
        if (idade>=18):
            print("Maior de idade")
            break
        else:
            print("Menor de idade")
            break
    except:
        print("Valor inválido!! Tente novamente")
        time.sleep(2)
        os.system('cls')

