import os,time
os.system('cls')

while True:
    try:
        print("===== Soma de 2 Números =====")
        num1 = int(input("Digite o 1º número: "))
        num2 = int(input("Digite o 2º número: "))

        soma = num1+num2
        print(f"Soma: {soma}")
        break
    except:
        print("Valor inválido!! tente novamente...")
        time.sleep(2)
        os.system('cls')
