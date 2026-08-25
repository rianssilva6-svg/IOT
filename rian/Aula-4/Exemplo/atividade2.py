import os
os.system('cls')
import time

lista = []

while True:
    print("===== Soma dos números com vetor =====")
    print("0 - sair")
    num = int(input("Digite um número: "))
    
    if num != 0:
        lista.append(num)
        os.system('cls')
    else:
        print("Finalizando o sistema...")
        time.sleep(3)
        break
        
soma = sum(lista)
print(f"A soma dos números digitados é: {soma}")

