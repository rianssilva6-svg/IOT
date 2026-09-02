import os,time
os.system('cls')

while True:
    try:
        print("===== Tabuada =====")
        num = int(input("Digite um número para a tabuada: "))
        for tabuada in range(10):
            resultado = ((tabuada+1)*num)
            print(f"{num} x {tabuada+1} = {resultado}")
        break
    except:
        print("Valor inválido!! Tente novamente")
        time.sleep(2)
        os.system('cls')
