import os
os.system('cls')

v_nomes = []

print("===== Registro de nomes =====")
for count in range(5):
    nome = input(f"Digite o {count+1}º nome: ")
    v_nomes.append(nome)
    
v_nomes.sort()
print(v_nomes)