import os
os.system('cls')
import time

while True:
    print("===== Registro de senha =====")
    senha = input("Digite uma senha de 4 digitos: ")
    quant_senha = len(senha)
    
    if quant_senha != 4:
        if senha.isdigit():
            print("Senha inválida")
            time.sleep(3)
            os.system('cls')
    else:
        print("Senha cadastrada com sucesso")
        time.sleep(3)
        break