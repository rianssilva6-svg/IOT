import os,time
os.system('cls')

while True:
    try:
        print("===== Saldo Bancário =====")
        saldo = float(input("Digite o seu saldo: "))
        saque = float(input("Digite quanto quer sacar: "))

        if (saldo >= saque):
            valor = (saldo-saque)
            print(f"Saque realizado com sucesso!!\nSaldo restante: {valor}")
            break
        else:
            print("Saldo insuficiente")
            time.sleep(2)
            os.system('cls')

    except:
        print("Digite apenas valores númericos")
        time.sleep(2)
        os.system('cls')