import random, os, time
os.system('cls')

num_secreto = random.randint(1,20)
tentativas = 0


while True:
    numero = int(input("Digite o número secreto: "))
    tentativas += 1
    
    if numero == num_secreto:
        print(f"Parabens!!! Você acertou o número em {tentativas}")
        time.sleep(2)
        break
    
    elif num_secreto > numero:
        print(f"O número secreto é maior!! - {tentativas} tentativas")
        time.sleep(2)
        os.system('cls')
    
    else:
        print(f"O número secreto é menor!! - {tentativas} tentativas")
        time.sleep(2)
        os.system('cls')