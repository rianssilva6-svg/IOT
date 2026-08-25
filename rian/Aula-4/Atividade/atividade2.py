import random, os
os.system('cls')

vetor_nomes = []

print("===== Sorteio =====")
for count in range (10):
    nome = input(f"Digite o {count+1}º nome: ")
    vetor_nomes.append(nome)
    os.system('cls')
    
ganhador = random.choice(vetor_nomes)
print(f"O ganhador foi: {ganhador}")