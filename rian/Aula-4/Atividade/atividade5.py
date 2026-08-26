import os
os.system('cls')
import time

while True:
    print("===== Registro de senha =====")
    senha = input("Cadastre uma senha de 4 digitos: ")
    quant_senha = len(senha)
    
    if quant_senha != 4:
        if senha.isdigit():
            print("Senha inválida")
            time.sleep(1)
            os.system('cls')
    else:
        print("Senha cadastrada com sucesso")
        time.sleep(1)
        break